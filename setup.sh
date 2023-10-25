user=$(logname)
cd ~
sudo cp /home/$user/TerminalStore/terminalstore /usr/local/bin/
cd /usr/local/bin/
sudo chmod +x terminalstore
sudo chmod +x /home/$user/TerminalStore/terminalstore.py