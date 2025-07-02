## bash
#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

# BLUX logo banner
cat << "EOF" > $HOME/.blux_banner
$(cat assets/blux_logo.txt)
EOF

# Add BLUX logo banner and color scheme to .bashrc
if ! grep -q ".blux_banner" $HOME/.bashrc; then
    echo 'cat $HOME/.blux_banner' >> $HOME/.bashrc
fi

# Set a BLUX color scheme (example: cyan prompt)
if ! grep -q "BLUX_THEME" $HOME/.bashrc; then
    echo 'export PS1="\[\e[36m\]\u@\h:\w\$ \[\e[m\]" # BLUX_THEME' >> $HOME/.bashrc
fi

echo "BLUX logo and theme applied to Termux!"

