# bash
#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

MODELS=(models/llama.cpp/models/*.gguf)
if [ ${#MODELS[@]} -eq 0 ]; then
    echo "No models found for benchmarking."
    exit 1
fi

echo "Benchmarking all models..."
for MODEL in "${MODELS[@]}"; do
    echo "Testing $MODEL"
    /usr/bin/time -v ./models/llama.cpp/main -m "$MODEL" -p "Test prompt" 2>&1 | tee "benchmark_${MODEL##*/}.log"
done
echo "Benchmark complete. See benchmark_*.log for details."

