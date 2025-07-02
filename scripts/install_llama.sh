# !/data/data/com.termux/files/usr/bin/bash
set -e

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
echo "✅ llama.cpp Installed Successfully!"
