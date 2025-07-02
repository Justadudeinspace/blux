## bash
#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "Installing Acode IDE (Android code editor)..."
pkg install -y xdg-utils
am start -a android.intent.action.VIEW -d "https://play.google.com/store/apps/details?id=com.foxdebug.acodefree"
echo "Acode IDE install intent sent. Please install from Play Store or F-Droid if not already present."

