#!/bin/bash

echo ""

if [ "$EUID" != 0 ]
  then
  echo "Not running as root, please run as root. (Exit code 0 or 128)"
  exit 128
fi

echo "ColourApp Installer for Debian Rev 3"
echo "This program installs ColourApp onto your system."
echo "ColourApp is available on GitHub: github.com/colourroot/colourapp"
echo "A temporary installation directory will be made as ~/capp-temp-install. This directory will be removed after installation."
echo "Installation will start in 10s. Press Ctrl+C to stop."
sleep 7s
echo "Installation will start in 3s. Press Ctrl+C to stop."
sleep 3s

echo "Section 0/4.  Install dependencies for installer. Installs: wget"
sudo apt install -y wget

echo "Section 1/4.  Install dependencies."
echo "Step    1/11. Install Qt5, Python3, PyQt5, Python 3 wget, Python 3 pip."
sudo apt-get install -y qt5-default python3 python3-pyqt5 python3-wget python3-pip > capp-install-debug.txt

echo "Section 2/4.  Prepare, download, unzip."
echo "Step    2/11. Create ~/capp-temp-install."
mkdir ~/capp-temp-install
echo "Step    3/11. Get ColourApp source from GitHub."
wget https://github.com/colourroot/colourapp/archive/master.zip -O ~/capp-temp-install/source.zip > capp-install-debug.txt
echo "Step    4/11. Unzip source."
unzip ~/capp-temp-install/source.zip -d ~/capp-temp-install/source > capp-install-debug.txt

echo "Section 3/4.  Move, set PATH."
echo "Step    5/10. Create /opt/colourroot/colourapp."
mkdir -p /opt/colourroot/colourapp
echo "Step    6/11. Move source to /opt/colourroot/colourapp."
mv ~/capp-temp-install/source/colourapp-master/* /opt/colourroot/colourapp
echo "Step    7/11. Remove ~/capp-temp-install."
rm -r ~/capp-temp-install
mv /opt/colourroot/colourapp/colourapp-master /opt/colourroot/colourapp
echo "Step    8/11. Touch ~/.colourroot_profile."
touch ~/.colourroot_profile
echo "Step    9/11. Enter PATH to ~/.colourroot_profile."
echo "PATH=\"/opt/colourroot/colourapp:$PATH\"" >> ~/.colourroot_profile
echo "Step    10/11. Check if source is already done on ~/.profile."
cat ~/.profile | grep "PATH=\"/opt/colourroot/colourapp:$PATH\""
echo "Step    11/11. If loop to check."
if [ $? != 0 ]; then
  echo "source ~/.colourroot_profile" >> ~/.profile
fi

echo "Section 4/4.  Validate."
echo "Step    11/11. Validate files. [Feature Not Available]"
echo "Feature is not available yet."

echo "Installation has finished."
echo "Visit github.com/colourroot/colourapp for more information."
