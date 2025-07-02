# bash
# !/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "🚀 Downloading DeepSeek GGUF..."
if [ -z "${HF_TOKEN:-}" ]; then
    echo "Please set your Hugging Face token in the environment (export HF_TOKEN=...)"
    exit 1
fi
mkdir -p models/llama.cpp/models
cd models/llama.cpp/models
wget --header="Authorization: Bearer $HF_TOKEN" \
"https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base-GGUF/resolve/main/ggml-vocab-deepseek-coder.gguf" \
-O ggml-vocab-deepseek-coder.gguf
if [ ! -f "ggml-vocab-deepseek-coder.gguf" ]; then
    echo "❌ Model download failed!"
    exit 1
fi
echo "✅ DeepSeek GGUF Downloaded!"

