#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "Benchmarking all models..."
for MODEL in models/llama.cpp/models/*.gguf; do
    echo "Testing $MODEL"
    /usr/bin/time -v ./models/llama.cpp/main -m "$MODEL" -p "Test prompt" 2>&1 | tee "benchmark_${MODEL##*/}.log"
done
echo "Benchmark complete. See benchmark_*.log for details."

