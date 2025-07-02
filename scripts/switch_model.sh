# bash
#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "Available models:"
ls models/llama.cpp/models/*.gguf 2>/dev/null || { echo "No models found."; exit 1; }
echo
read -p "Enter model filename to use (e.g., ggml-vocab-deepseek-coder.gguf): " MODEL
if [ ! -f "models/llama.cpp/models/$MODEL" ]; then
    echo "Model not found!"
    exit 1
fi
echo "$MODEL" > models/llama.cpp/models/active_model.txt
echo "Active model set to $MODEL"

