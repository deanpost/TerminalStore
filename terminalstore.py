#This took so long to make
import readline
import os
print()
print("TerminalStore Version 0.2.2 Nightly")
print("New here?: Do /help for to get started!")
while True:
    print()
    usrinp = input("command# ")
    print()
    
    if (usrinp == "/update"):
        print ("Updating your system...")
        print ("This may ask for your sudo password.")
        os.system ('sudo apt-get update')
        print ("Done!")

    elif (usrinp == "/clear"):
        os.system ('clear')

    elif (usrinp == "/quit"):
        print ('Thanks for using TerminalStore!')
        print("Quitting TerminalStore...")
        exit()

    elif (usrinp == "/startscreen"):
        os.system('clear')
        print("TerminalStore Version 0.2.2 Nightly")
        print("New here?: Do /help for to get started!")

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

    #Greed
    elif (usrinp == "/install greed"):
        print("Installing Greed...")
        os.system ('sudo apt install greed')
        print("Done!")

    #BSDGames
    elif (usrinp == "/install bsdgames"):
        print("Installing BSDGames...")
        os.system ('sudo apt install bsdgames')
        print("Done!")

    #Moon Buggy
    elif (usrinp == "/install moon-buggy"):
        print("Installing Moon Buggy...")
        os.system ('sudo apt install moon-buggy')
        print("Done!")

    #2048
    elif (usrinp == "/install 2048"):
        print("Installing 2048...")
        os.system ('cd ~/TerminalStore && sudo bash 2048.sh')
        print("Done!")

    #Nudoku
    elif (usrinp == "/install nudoku"):
        print("Installing Nudoku...")
        os.system ('sudo apt install nudoku')
        print("Done!")

    #ScratchLang
    elif (usrinp == "/install scratchlang"):
        print("Installing ScratchLang...")
        os.system ('cd ~/TerminalStore && sudo bash sl.sh')
        print("Done!")

    #Vim
    elif (usrinp == "/install vim"):
        print("Installing Vim...")
        os.system ('sudo apt install vim')
        print("Done!")

    #Vim-tiny
    elif (usrinp == "/install vim-tiny"):
        print("Installing Vim-tiny...")
        os.system ('sudo apt install vim-tiny')
        print("Done!")

    #Vim-nox
    elif (usrinp == "/install vim-nox"):
        print("Installing Vim...")
        os.system ('sudo apt install vim-nox')
        print("Done!")

    #Emacs-nox
    elif (usrinp == "/install emacs-nox"):
        print("Installing Emacs-nox...")
        os.system ('sudo apt install emacs-nox')
        print("Done!")

    #micro
    elif (usrinp == "/install micro"):
        print("Installing micro...")
        os.system ('curl https://getmic.ro | bash')
        print("Done!")

    #orbiton
    elif (usrinp == "/install orbiton"):
        print("Installing orbiton...")
        os.system ('go install github.com/xyproto/orbiton/v2@latest && mv -i ~/go/bin/orbiton ~/go/bin/o')
        print("Done!")

    #kakoune
    elif (usrinp == "/install kakoune"):
        print("Installing kakoune...")
        os.system ('cd ~/TerminalStore && sudo bash kakoune.sh')
        print("Done!")

    #helix
    elif (usrinp == "/install emacs-nox"):
        print("Installing Emacs-nox...")
        os.system ('cd ~/TerminalStore && sudo bash helix.sh')
        print("Done!")

    #NeoVim
    elif (usrinp == "/install neovim"):
        print("Installing NeoVim...")
        os.system ('sudo apt install neovim')
        print("Done!")

    #cmus
    elif (usrinp == "/install cmus"):
        print("sudo bash cmus.sh")
        os.system ('sudo apt install vim')
        print("Done!")

    #Instant-Music-Downloader
    elif (usrinp == "/install instant-music-downloader"):
        print("Installing Instant-Music-Downloader...")
        os.system ('$ pip3 install instantmusic')
        print("Done!")

    #pianobar
    elif (usrinp == "/install pianobar"):
        print("Installing pianobar...")
        os.system ('cd ~/TerminalStore && sudo bash pianobar.sh')
        print("Done!")
        #needs tbd

    #somafm-cli
    elif (usrinp == "/install somafm-cli"):
        print("Installing somafm-cli...")
        os.system ('cd ~/TerminalStore && sudo bash somafm-cli.sh')
        print("Done!")

    #Music Player Daemon
    elif (usrinp == "/install mpd"):
        print("Installing Music Player Daemon...")
        os.system ('sudo apt install mpd')
        print("Done!")

    #NCurses Music Player Client (Plus Plus)
    elif (usrinp == "/install ncmpcpp"):
        print("Installing NCurses Music Player Client (Plus Plus)...")
        os.system ('cd ~/TerminalStore && sudo bash ncmpcpp.sh')
        print("Done!")

    #MOC
    elif (usrinp == "/install moc"):
        print("Installing MOC...")
        os.system ('sudo apt install moc')
        print("Done!")

    #musikcube
    elif (usrinp == "/install musikcube"):
        print("Installing musikcube...")
        os.system ('cd ~/TerminalStore && sudo bash musikcube.sh')
        print("Done!")

    #beets
    elif (usrinp == "/install beets"):
        print("Installing beets...")
        os.system ('sudo apt install beets')
        print("Done!")

    #Spotify TUI
    elif (usrinp == "/install spotify-tui"):
        print("Installing Spotify TUI...")
        os.system ('snap install spt')
        print("Done!")

    #SwagLyrics-For-Spotify
    elif (usrinp == "/install swagLyrics-for-spotify"):
        print("Installing SwagLyrics-For-Spotify...")
        os.system ('pip install swaglyrics')
        print("Done!")

    #dzr
    elif (usrinp == "/install dzr"):
        print("Installing dzr...")
        os.system ('snap install --edge dzr')
        print("Done!")

    #RADIOACTIVE
    elif (usrinp == "/install radio-active"):
        print("Installing RADIOACTIVE...")
        os.system ('cd ~/TerminalStore && sudo bash radio-active.sh')
        print("Done!")

    #youtube-dl
    elif (usrinp == "/install youtube-dl"):
        print("Installing youtube-dl...")
        os.system ('cd ~/TerminalStore && sudo bash youtube-dl.sh')
        print("Done!")

    #streamlink
    elif (usrinp == "/install streamlink"):
        print("Installing streamlink...")
        os.system ('sudo apt install streamlink')
        print("Done!")

    #yewtube
    elif (usrinp == "/install yewtube"):
        print("Installing yewtube...")
        os.system ('pip install yewtube')
        print("Done!")

    #mpv
    elif (usrinp == "/install mpv"):
        print("Installing mpv...")
        os.system ('sudo apt install mpv')
        print("Done!")

    #editly
    elif (usrinp == "/install youtube-dl"):
        print("Installing youtube-dl...")
        os.system ('npm i -g editly')
        print("Done!")

    #yt-dlp
    elif (usrinp == "/install yt-dlp"):
        print("Installing yt-dlp...")
        os.system ('pip install yt-dlp')
        print("Done!")

    #moviemon
    elif (usrinp == "/install moviemon"):
        print("Installing moviemon...")
        os.system ('pip install moviemon')
        print("Done!")

    #movie
    elif (usrinp == "/install movie"):
        print("Installing movie...")
        os.system ('npm i -g movie-cli')
        print("Done!")

    #Dwarf Fortress
    elif (usrinp == "/install yt-dlp"):
        print("Installing yt-dlp...")
        os.system ('pip install yt-dlp')
        print("Done!")
    
    #pokete
    elif (usrinp == "/install pokete"):
        print("Installing pokete...")
        os.system ('cd ~/TerminalStore && sudo bash pokete.sh')
        print("Done!")

    #epr
    elif (usrinp == "/install epr"):
        print("Installing epr...")
        os.system ('pip3 install epr-reader')
        print("Done!")

    #Bible.JS CLI
    elif (usrinp == "/install bible-js-cli"):
        print("Installing Bible.JS CLI...")
        os.system ('npm i bible')
        print("Done!")

    #SpeedRead
    elif (usrinp == "/install speedread"):
        print("Installing SpeedRead...")
        os.system ('$ gem install speed_read')
        print("Done!")

    #medium-cli
    elif (usrinp == "/install medium-cli"):
        print("Installing medium-cli...")
        os.system ('npm install -g mediumcli')
        print("Done!")

 #/apps command
    elif (usrinp == "/apps"):
        print()
        print ("Apps:")
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
        print ("Greed (/info greed for more info)")
        print ("nudoku (/info nudoku for more info)")
        print ("2048 (/info 2048 for more info)")
        print ("Moon Buggy (/info moon-buggy for more info)")
        print()
        print ('Game packages:')
        print ('BSDGames (/info bsdgames for more info)')
        print()
        print ("Text editors:")
        print ("Vim (/info vim for more info)")
        print ("Vim-tiny (/info vim-tiny for more info)")
        print ("Vim-nox (/info vim-nox for more info)")
        print ("NeoVim (/info neovim for more info)")
        print ("Emacs-nox (/info rmacs-nox for more info)")
        print ("Kakoune (/info kakoune for more info)")
        print ("micro (/info micro for more info)")
        print ("orbiton (/info orbiton for more info)")
        print ("Helix (/info helix for more info)")
        print()
        print ("Programming languages:")
        print("ScratchLang (/info scratchlang for more info)")
        print()
        print ('Music:')
        print ("cmus (/info cmus for more info)")
        print ("Instant-Music-Downloader (/info instant-music-downloader for more info)")
        print ("pianobar (/info pianobar for more info)")
        print ("somafm-cli (/info somafm-cli for more info)")
        print ("Music Player Daemon (/info music-player-daemon for more info)")
        print ("NCurses Music Player Client (Plus Plus) (/info ncmpcpp for more info)")
        print ("MOC (/info moc for more info)")
        print ("musikcube (/info musikcube for more info)")
        print ("Beets (/info beets for more info)")
        print ("Spotify Tui (/info spotify-tui for more info)")
        print ("SwagLyrics-For-Spotify (/info swagLyrics-for-spotify for more info)")
        print ("DZR (/info dzr for more info)")
        print ("RADIO-ACTIVE (/info radio-active for more info)")
        print()
        print('Social Media:')
        print ("Facebook CLI (/info facebook-cli for more info)")
        print ("Rainbow Stream (/info rainbowstream for more info)")
        print ("tuir (/info tuir for more info)")
        print ("WeeChat (/info weechat for more info)")
        print ("Irssi (/info irssi for more info)")
        print ("kirc (/info kirc for more info)")
        print()
        print('Video:')
        print ("youtube-dl (/info youtube-dl for more info)")
        print ("Streamlink (/info streamlink for more info)")
        print ("yewtube (/info yewtube for more info)")
        print ("yt-dlp (/info yt-dlp for more info)")
        print()
        print('Movies:')
        print ("Moviemon (/info moviemon for more info)")
        print ("movie (/info movie for more info)")
        print()
        print('Books:')
        print ("epr (/info epr for more info)")
        print ("Bible.Js CLI (/info bible-js-cli for more info)")
        print ("SpeedRead (/info speedread for more info)")
        print ("medium-cli (/info medium-cli for more info)")
        

    elif (usrinp == "/version"):
        print ("Current version: 0.2.1 Nightly")

 #/info commmands
    elif (usrinp == "/info"):
        print ("Usage: /info test1 for info of test1")
    #test1
    elif (usrinp == "/info test1"):
        print ("Name: test1")
        print ("Version: 1.0")
        print ("Description: Itz an app lol")
        print ("Website: https://github.com/deanpost/")
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

    #Greed
    elif (usrinp == "/info greed"):
        print ("Name: Greed")
        print ("Description: Greed is a little like Tron, minus the speed and adrenaline.")
        print ("Website: https://manpages.ubuntu.com/manpages/focal/man6/greed.6.html")
        print ("Type /install greed to install greed")

    #BSDGames
    elif (usrinp == "/info bsdgames"):
        print ("Name: BSDGames")
        print ("Description: Collection of classic textual unix games.")
        print ("Website: https://github.com/vattam/BSDGames")
        print ("Type /install bsdgames to install bsdgames")

    #Moon Buggy
    elif (usrinp == "/info moon-buggy"):
        print ("Name: Moon Buggy")
        print ("Description: Jump. Fire. Hours of fun. No more words to describe it. Lots of fun!")
        print ("Website: https://www.seehuhn.de/pages/moon-buggy")
        print ("Type /install moon-buggy to install moon-buggy")

    #2048
    elif (usrinp == "/info 2048"):
        print ("Name: 2048")
        print ("Description: 2048 is a strategic as well as highly addictive game. The goal is to get a score of 2048.")
        print ("Website: https://github.com/mevdschee/2048.c")
        print ("Type /install 2048 to install 2048")

    #nudoku
    elif (usrinp == "/info nudoku"):
        print ("Name: nudoku")
        print ("Description: Want to play Sudoku on the Linux terminal? Why not.")
        print ("Website: http://jubalh.github.io/nudoku/")
        print ("Type /install nudoku to install nudoku")

    #Dwarf Fortress
    elif (usrinp == "/info dwarf-fortress"):
        print ("Name: Dwarf Fortress")
        print ("Description: The deepest, most intricate simulation of a world that's ever been created.")
        print ("Website: http://www.bay12games.com/dwarves/")
        print ("Type /install dwarf-fortress to install dwarf-fortress")

    #pokete
    elif (usrinp == "/info pokete"):
        print ("Name: pokete")
        print ("Description: A terminal based Pokemon like game.")
        print ("Website: https://lxgr-linux.github.io/pokete/")
        print ("Type /install pokete to install pokete")

    #ScratchLang
    elif (usrinp == "/info scratchlang"):
        print ("Name: ScratchLang")
        print ("Description: Scratch as a Text-Based Programming Language.")
        print ("Website: https://github.com/ScratchLang/")
        print ("Type /install scratchlang to install scratchlang")

    #Vim
    elif (usrinp == "/info vim"):
        print ("Name: Vim")
        print ("Description: Vi IMproved - enhanced vi editor.")
        print ("Website: https://www.vim.org/")
        print ("Type /install scratchlang to install scratchlang")

    #Vim-tiny
    elif (usrinp == "/info vim-tiny"):
        print ("Name: Vim-tiny")
        print ("Description: Vi IMproved - enhanced vi editor - compact version.")
        print ("Website: https://www.vim.org/")
        print ("Type /install vim-tiny to install vim-tiny")

    #Vim-nox
    elif (usrinp == "/info vim-nox"):
        print ("Name: Vim-nox")
        print ("Description: Vi IMproved - enhanced vi editor - with scripting languages support.")
        print ("Website: https://www.vim.org/")
        print ("Type /install vim-nox to install vim-nox")

    #NeoVim
    elif (usrinp == "/info neovim"):
        print ("Name: NeoVim")
        print ("Description: hyperextensible Vim-based text editor.")
        print ("Website: https://neovim.io/")
        print ("Type /install neovim to install neovim")

    #Emacs-nox
    elif (usrinp == "/info emacs-nox"):
        print ("Name: Emacs-nox")
        print ("Description: An extensible, customizable, free/libre text editor.")
        print ("Website: https://www.gnu.org/software/emacs/")
        print ("Type /install emacs-nox to install emacs-nox")

    #Kakoune
    elif (usrinp == "/info kakoune"):
        print ("Name: Kakoune")
        print ("Description: Modal editor, Faster as in fewer keystrokes, Multiple selections, Orthogonal design")
        print ("Website: https://kakoune.org/")
        print ("Type /install kakoune to install kakoune")

    #micro
    elif (usrinp == "/info micro"):
        print ("Name: micro")
        print ("Description: a modern and intuitive terminal-based text editor.")
        print ("Website: https://micro-editor.github.io/")
        print ("Type /install micro to install micro")
    
    #orbiton
    elif (usrinp == "/info orbiton"):
        print ("Name: orbiton")
        print ("Description: Fast and config-free text editor and IDE limited to VT100.")
        print ("Website: https://github.com/xyproto/orbiton")
        print ("Type /install orbiton to install orbiton")

    #Helix
    elif (usrinp == "/info helix"):
        print ("Name: helix")
        print ("Description: A post-modern modal text editor. ")
        print ("Website: https://helix-editor.com/")
        print ("Type /install helix to install helix")

    #cmus
    elif (usrinp == "/info cmus"):
        print ("Name: cmus")
        print ("Description: mus is a small, fast and powerful console music player for Unix-like operating systems.")
        print ("Website: https://cmus.github.io/")
        print ("Type /install cmus to install cmus")

    #Instant-Music-Downloader
    elif (usrinp == "/info instant-music-downloader"):
        print ("Name: Instant-Music-Downloader")
        print ("Description: Instantly download any song!")
        print ("Website: http://iyask.me/Instant-Music-Downloader/")
        print ("Type /install instant-music-downloader to install instant-music-downloader")

    #pianobar
    elif (usrinp == "/info pianobar"):
        print ("Name: pianobar")
        print ("Description: pianobar is a free/open-source, console-based client for the personalized online radio Pandora.")
        print ("Website: https://6xq.net/pianobar/")
        print ("Type /install pianobar to install pianobar")

    #somafm-cli
    elif (usrinp == "/info somafm-cli"):
        print ("Name: somafm-cli")
        print ("Description: Listen to SomaFM in your terminal via pure bash.")
        print ("Website: https://github.com/rockymadden/somafm-cli")
        print ("Type /install somafm-cli to install somafm-cli")

    #Music Player Daemon
    elif (usrinp == "/info music-player-daemon"):
        print ("Name: Music Player Daemon")
        print ("Description: Music Player Daemon (MPD) is a flexible, powerful, server-side application for playing music.")
        print ("Website: https://www.musicpd.org/")
        print ("Type /install music-player-daemon to install music-player-daemon")

    #NCurses Music Player Client (Plus Plus)
    elif (usrinp == "/info ncmpcpp"):
        print ("Name: NCurses Music Player Client (Plus Plus)")
        print ("Description: Featureful ncurses based MPD client inspired by ncmpc.")
        print ("Website: https://rybczak.net/ncmpcpp/")
        print ("Type /install ncmpcpp to install ncmpcpp")

    #MOC
    elif (usrinp == "/info moc"):
        print ("Name: MOC")
        print ("Description: Console audio player for Linux/UNIX.")
        print ("Website: http://moc.daper.net/")
        print ("Type /install moc to install moc")

    #musikcube
    elif (usrinp == "/info musikcube"):
        print ("Name: musikcube")
        print ("Description: musikcube is a fully functional terminal-based music player.")
        print ("Website: https://musikcube.com/")
        print ("Type /install musikcube to install musikcube")

    #musikcube
    elif (usrinp == "/info musikcube"):
        print ("Name: musikcube")
        print ("Description: musikcube is a fully functional terminal-based music player.")
        print ("Website: https://musikcube.com/")
        print ("Type /install musikcube to install musikcube")

    #Beets
    elif (usrinp == "/info beets"):
        print ("Name: Beets")
        print ("Description: Beets is the media library management system for obsessive music geeks.")
        print ("Website: https://beets.io/")
        print ("Type /install beets to install beets")

    #Spotify Tui
    elif (usrinp == "/info spotify-tui"):
        print ("Name: Spotify Tui")
        print ("Description: A Spotify client for the terminal written in Rust.")
        print ("Website: https://github.com/Rigellute/spotify-tui/")
        print ("Type /install spotify-tui to install spotify-tui")

    #SwagLyrics-For-Spotify
    elif (usrinp == "/info swagLyrics-for-spotify"):
        print ("Name: SwagLyrics-For-Spotify")
        print ("Description: Fetches the currently playing song from Spotify on Windows, Linux and macOS and displays the lyrics in the command-line or in a browser tab.")
        print ("Website: https://pypi.org/project/swaglyrics/")
        print ("Type /install swagLyrics-for-spotify to install swagLyrics-for-spotify")

    #DZR
    elif (usrinp == "/info dzr"):
        print ("Name: DZR")
        print ("Description: DZR: the command line deezer.com player.")
        print ("Website: https://github.com/yne/dzr")
        print ("Type /install dzr to install dzr")

    #RADIO-ACTIVE
    elif (usrinp == "/info radio-active"):
        print ("Name: RADIO-ACTIVE")
        print ("Description: Play any radios around the globe right from your terminal.")
        print ("Website: https://www.radio-browser.info/#/")
        print ("Type /install radio-active to install radio-active")

    #Facebook CLI
    elif (usrinp == "/info facebook-cli"):
        print ("Name: Facebook CLI")
        print ("Description: Facebook functionality from the command line.")
        print ("Website: https://github.com/specious/facebook-cli")
        print ("Type /install facebook-cli to install facebook-cli")

    #Rainbow Stream
    elif (usrinp == "/info rainbowstream"):
        print ("Name: Rainbow Stream")
        print ("Description: A smart and nice Twitter client on terminal written in Python.")
        print ("Website: https://github.com/orakaro/rainbowstream")
        print ("Type /install rainbowstream to install rainbowstream")

    #tuir
    elif (usrinp == "/info tuir"):
        print ("Name: tuir")
        print ("Description: Browse Reddit from your terminal.")
        print ("Website: https://gitlab.com/ajak/tuir")
        print ("Type /install tuir to install tuir")

    #WeeChat
    elif (usrinp == "/info weechat"):
        print ("Name: WeeChat")
        print ("Description: WeeChat, the extensible chat client.")
        print ("Website: https://weechat.org/")
        print ("Type /install weechat to install weechat")

    #Irssi
    elif (usrinp == "/info irssi"):
        print ("Name: Irssi")
        print ("Description: The client of the future.")
        print ("Website: https://irssi.org/")
        print ("Type /install irssi to install irssi")

    #kirc
    elif (usrinp == "/info kirc"):
        print ("Name: kirc")
        print ("Description: A tiny IRC client written in POSIX C99.")
        print ("Website: https://mcpcpc.github.io/kirc/")
        print ("Type /install kirc to install kirc")

    #youtube-dl
    elif (usrinp == "/info youtube-dl"):
        print ("Name: youtube-dl")
        print ("Description: Streamlink is a CLI utility which pipes video streams from various services into a video player.")
        print ("Website: http://ytdl-org.github.io/youtube-dl/")
        print ("Type /install youtube-dl to install youtube-dl")

    #Streamlink
    elif (usrinp == "/info streamlink"):
        print ("Name: Streamlink")
        print ("Description: Streamlink is a CLI utility which pipes video streams from various services into a video player.")
        print ("Website: https://streamlink.github.io/")
        print ("Type /install streamlink to install streamlink")

    #yewtube
    elif (usrinp == "/info yewtube"):
        print ("Name: yewtube")
        print ("Description: Terminal based YouTube player and downloader.")
        print ("Website: https://github.com/mps-youtube/yewtube/")
        print ("Type /install yewtube to install yewtube")

    #yt-dlp
    elif (usrinp == "/info yt-dlp"):
        print ("Name: yt-dlp")
        print ("Description: A youtube-dl fork with additional features and fixes.")
        print ("Website: https://github.com/yt-dlp/yt-dlp/")
        print ("Type /install yt-dlp to install yt-dlp")

    #Moviemon
    elif (usrinp == "/info moviemon"):
        print ("Name: Moviemon")
        print ("Description: Everything about your movies within the command line.")
        print ("Website: https://ichait.github.io/moviemon/")
        print ("Type /install moviemon to install moviemon")

    #movie
    elif (usrinp == "/info movie"):
        print ("Name: movie")
        print ("Description: CLI for getting information about movies and comparing two movies.")
        print ("Website: https://github.com/mayankchd/movie/")
        print ("Type /install movie to install movie")

    #epr
    elif (usrinp == "/info epr"):
        print ("Name: epr")
        print ("Description: CLI Epub Reader.")
        print ("Website: https://github.com/wustho/epr/")
        print ("Type /install epr to install epr")

    #Bible.Js CLI
    elif (usrinp == "/info bible-js-cli"):
        print ("Name: Bible.Js CLI")
        print ("Description: Read the Holy Bible via the command line.")
        print ("Website: https://github.com/BibleJS/BibleApp")
        print ("Type /install bible-js-cli to install bible-js-cli")

    #SpeedRead
    elif (usrinp == "/info speedread"):
        print ("Name: SpeedRead")
        print ("Description: A simple terminal-based open source Spritz-alike.")
        print ("Website: https://github.com/sunsations/speed_read")
        print ("Type /install speedread to install speedread")

    #medium-cli
    elif (usrinp == "/info medium-cli"):
        print ("Name: medium-cli")
        print ("Description: Medium for Hackers - A CLI for reading Medium Stories.")
        print ("Website: https://github.com/djadmin/medium-cli")
        print ("Type /install medium-cli to install medium-cli")

    #bsdgames apps
    #COMING LATER

    #adventure
    elif (usrinp == "/info adventure"):
        print ("Name: Adventure")
        print ("Description: the original adventure by Crowther and Woods")
        print ("Website: https://github.com/vattam/BSDGames")
        print ("Type /install bsdapps to install adventure")



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
        print("Sorry, but we dont know: " + usrinp + ". Maybe try /help for help!")
    
