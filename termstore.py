#WIP
import os
while True:
    print()
    print("TerminalStore Version 0.1 dev_test (Work in progress)")
    usrinp = input("command# ")
    print ()
    
    if (usrinp == "/update"):
        print ("Updating your system...")
        print ("This may ask for your sudo password.")
        os.system ('sudo apt-get update')
        print ("Done!")

    elif (usrinp == "/clear"):
        os.system ('clear')

    elif (usrinp == "/quit"):
        print("Quitting TerminalStore...")
        exit()
  #/install commands      
    elif (usrinp == "/install"):
        print ("Usage: /install test1 to install test1")
    #test1    
    elif (usrinp == "/install test1"):
        print("Installing test1...")
        os.system ('sudo apt-get update')
        print("Done!")
    #w3m
    elif (usrinp == "/install w3m"):
        print("Installing w3m...")
        os.system ('sudo apt install w3m w3m-img')
        print("Done!")
    #lynx
    elif (usrinp == "/install lynx"):
        print("Installing lynx...")
        os.system ('sudo apt install lynx')
        print("Done!")
    #Links2
    elif (usrinp == "/install links2"):
        print("Installing Links2...")
        os.system ('sudo apt install links2')
        print("Done!")

    #eLinks
    elif (usrinp == "/install elinks"):
        print("Installing eLinks...")
        os.system ('sudo apt install elinks')
        print("Done!")

    #Bastet
    elif (usrinp == "/install bastet"):
        print("Installing Bastet...")
        os.system ('sudo apt install bastet')
        print("Done!")

    #Ninvaders
    elif (usrinp == "/install ninvaders"):
        print("Installing Ninvaders...")
        os.system ('sudo apt install ninvaders')
        print("Done!")

    #Pacman4console
    elif (usrinp == "/install pacman4console"):
        print("Installing Pacman4console...")
        os.system ('sudo apt install pacman4console')
        print("Done!")

    #nSnake
    elif (usrinp == "/install nsnake"):
        print("Installing nSnake...")
        os.system ('sudo apt install nsnake')
        print("Done!")



    elif (usrinp == "/apps"):
        print ("Apps:")
        print()
        print ("Web Browsers:")
        print ("w3m (/info w3m for more info)")
        print ("lynx (/info lynx for more info)")
        print ("Links2 (/info links2 for more info)")
        print ("eLinks (/info elinks for more info)")
        print()
        print ("Games:")
        print ("Bastet (/info bastet for more info)")
        print ("Ninvaders (/info ninvaders for more info)")
        print ("Pacman4console (/info pacman4console for more info)")
        print ("nSnake (/info nsnake for more info)")
        print()
        print("More apps will be added soon!")

    elif (usrinp == "/version"):
        print ("Current version: 0.1 dev_test")
# /info commmands
    elif (usrinp == "/info"):
        print ("Usage: /info test1 for info of test1")
    #test1
    elif (usrinp == "/info test1"):
        print ("Name: test1")
        print ("Version: 1.0")
        print ("Description: Itz an app lol")
        print ("Website: https://github.com/RealW1-F1/test1")
        print ("Size: 1mb")
    #w3m
    elif (usrinp == "/info w3m"):
        print ("Name: w3m")
        print ("Description: Open-source text based web-browser")
        print ("Website: https://w3m.sourceforge.net/")
        print ("Type /install w3m to install w3m")
    #lynx
    elif (usrinp == "/info lynx"):
        print ("Name: lynx")
        print ("Description: Lynx is the text web browser")
        print ("Website: https://lynx.invisible-island.net/")
        print ("Type /install lynx to install lynx")

    #Links2
    elif (usrinp == "/info links2"):
        print ("Name: Links2")
        print ("Description: Links is a web browser running in both graphics and text mode.")
        print ("Website: http://links.twibright.com/")
        print ("Type /install links2 to install links2")

    #eLinks
    elif (usrinp == "/info elinks"):
        print ("Name: eLinks")
        print ("Description: ELinks is an advanced and well-established feature-rich text mode web (HTTP/FTP/..) browser.")
        print ("Website: http://elinks.or.cz/")
        print ("Type /install elinks to install elinks")

    #Bastet
    elif (usrinp == "/info bastet"):
        print ("Name: Bastet")
        print ("Description: Bastet is the Tetris of Linux.")
        print ("Website: http://fph.altervista.org/prog/bastet.html")
        print ("Type /install bastet to install bastet")

    #Ninvaders
    elif (usrinp == "/info ninvaders"):
        print ("Name: Ninvaders")
        print ("Description: Space Invaders on a command-line interface.")
        print ("Website: https://ninvaders.sourceforge.net/")
        print ("Type /install ninvaders to install ninvaders")

    #Pacman4console
    elif (usrinp == "/info pacman4console"):
        print ("Name: Pacman4console")
        print ("Description: King of the arcade.")
        print ("Website: https://github.com/YoctoForBeaglebone/pacman4console")
        print ("Type /install pacman4console to install pacman4console")

    #nSnake
    elif (usrinp == "/info nsnake"):
        print ("Name: nSnake")
        print ("Description: Remember the snake game on Nokia phones?")
        print ("Website: https://github.com/alexdantas/nSnake")
        print ("Type /install nsnake to install nsnake")


    
    elif (usrinp == "/help"):
        print ("Welcome to the help menu!")
        print ("/apps: Shows the number of apps you can install!")
        print ("/help: Shows the help menu!")
        print ("/update: Updates your OS!")
        print ("/install: shows the apps you can install (like /apps)")
        print ("/clear: Clears the screen")
        print ("/quit: Quits TerminalStore")
        print ("/credits: Shows the credits")
        print ("/version: Shows the version of TerminalStore")
        
    elif (usrinp == "/credits"):
        print("Developers:")
        print ("W1-F1 (Dean Post)")
        print ("Holly Post")
        print ("(C) Dean Post 2023")
        print ("Licensed under the GNU General Public License v3.0")
        print ("https://github.com/deanpost/TerminalStore")
        
    else:
        print("Sorry, put we dont know: " + usrinp + ". Maybe try /help for help!")
        print()
    