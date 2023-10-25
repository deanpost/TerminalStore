user=$(logname)
cd ~
sudo cp /home/$user/TerminalStore/terminalstore /usr/bin/
cd /usr/bin/
sudo chmod +x terminalstore
sudo chmod +x /home/$user/TerminalStore/terminalstore.py
