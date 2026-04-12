#!/bin/bash

MODEL_PATH="/path/to/weights"

PORT=8000

# 1. 后台启动 vLLM 服务
echo "正在启动 vLLM 服务..."

python -m vllm.entrypoints.openai.api_server \
    --model $MODEL_PATH \
    --port $PORT \
    --dtype bfloat16 \
    --trust-remote-code > vllm.log 2>&1 &

# 获取后台进程 PID
VLLM_PID=$!

# 2. 周期性检测服务状态
echo "等待服务就绪..."

while true; do
    if curl -s -o /dev/null -d '' http://localhost:$PORT/v1/chat/completions; then
        echo "✅ vLLM 服务已就绪！"
        # 持续输出日志并等待进程
        tail -f vllm.log
        wait $VLLM_PID
        exit 0
    fi

    # 检查进程是否意外挂掉（防止路径写错等导致的死循环）
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "❌ 错误：vLLM 进程已停止，请检查 vllm.log 日志。"
        exit 1
    fi

    echo "服务加载中，5秒后重试..."
    sleep 5
done