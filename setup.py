import os
print("TerminalStore installer")
print("Installing TerminalStore...")
#For bugtesting
#print("Your /usr/bin path(s)")
#os.system('echo ${PATH}')
os.system('cd ~')
os.system('sudo cp terminalstore /usr/local/bin/')
os.system('cd /usr/local/bin/')
os.system('sudo chmod +x terminalstore')
os.system('sudo chmod +x ~/TerminalStore/terminalstore.py')
print("Done!")
     
