#!/bin/bash

echo "🔮 Starting BLUX..."

# Activate web UI if desired
if [ "$1" == "web" ]; then
    export BLUX_WEB=1
fi

# Activate voice if desired
if [ "$1" == "voice" ]; then
    export BLUX_VOICE=1
fi

python3 -m blux.blux

