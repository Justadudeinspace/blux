# bash
# !/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "🚀 Installing llama.cpp..."
pkg install -y git clang cmake make
mkdir -p models
cd models
if [ ! -d "llama.cpp" ]; then
    git clone https://github.com/ggerganov/llama.cpp.git
fi
cd llama.cpp
make clean
make LLAMA_NATIVE=1
if [ ! -f "main" ]; then
    echo "❌ llama.cpp build failed!"
    exit 1
fi
echo "✅ llama.cpp Installed Successfully!"

