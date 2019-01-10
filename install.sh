#!/bin/bash

echo "This program install ColourApp onto your system."
echo "ColourApp is available on GitHub: github.com/colourroot/colourapp"
echo "A temporary installation directory will be made as ~/capp-temp-install. This directory will be removed after installation."
echo "Installation will start in 10s. Press Ctrl+C to stop."
sleep 7s
echo "Installation will start in 3s. Press Ctrl+C to stop."
sleep 3s

echo "Section 1/4.  Install dependencies."
echo "Step    1/11. Install Qt5, Python3, PyQt5, Python 3 wget, Python 3 pip."
sudo apt-get install -y qt5-default python3 python3-pyqt5 python3-wget python3-pip

echo "Section 2/4.  Prepare, download, unzip."
echo "Step    2/10. Create ~/capp-temp-install."
mkdir ~/capp-temp-install
echo "Step    3/10. Get ColourApp source from GitHub."
wget https://github.com/colourroot/colourapp/archive/master.zip -O ~/capp-temp-install/source.zip
echo "Step    4/10. Unzip source."
unzip ~/capp-temp-install/source.zip -d ~/capp-temp-install/source

echo "Section 3/4.  Move, set PATH."
echo "Step    5/10. Create /opt/colourroot/colourapp."
mkdir -p /opt/colourroot/colourapp
echo "Step    6/10. Move source to /opt/colourroot/colourapp."
mv ~/capp-temp-install/source /opt/colourroot/colourapp
echo "Step    7/10. Touch ~/.colourroot_profile."
touch ~/.colourroot_profile
echo "Step    8/10. Enter PATH to ~/.colourroot_profile."
echo "PATH=\"/opt/colourroot/colourapp:$PATH\"" >> ~/.colourroot_profile
echo "Step    9/10. Check if source is already done on ~/.profile."
cat ~/.profile | grep "PATH=\"/opt/colourroot/colourapp:$PATH\""
echo "Step    10/10. If loop to check."
if [ $? != 0 ]; then
  echo "source ~/.colourroot_profile" >> ~/.profile
fi

echo "Section 4/4.  Validate."
echo "Step    11/11. Validate files. [Feature Not Available]"
echo "Feature is not available yet."

echo "Installation has finished."
echo "Visit github.com/colourroot/colourapp for more information."
