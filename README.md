# Yeelight-rgb-bulb-controler
This program was made by Atae Kurri in 2020 using yeelight python library.

# How to use command-lines

<s>This program is command-line based, it means it has no graphical interface for the moment.
You can use multiple commands to control your rgb yeelight bulb.</s>
This program is using both commands and graphical interface (well, ugly but still functionnal) to control your rgb yeelight bulb.

To use your bulb in the program, in your yeelight or mihome application on your smartphone, please turn on remote control from local network. Overwise it'll not work at all and the bulb will not accept any commands from the program.

Use this program in Cmd, not directly, it will not work and just close. It's a command-line based program using argparse.
In cmd type "appCmd.py -h" for the list of commands.
You will need json ; argparse ; yeelight python modules to make to program work correctly
  
There is an config.json filled with examples, feel free to delete or modify them to your liking.
But please, don't delete the config.json file or the program will no longer work


Please keep in mind using this program that i'm not an experienced programer, but I do my best, there is some errors that i can't seem to be able at the time to contain or explain in plain text. Keep in mind that the english translation is not perfect, being french.

# How to use the graphical interface

The graphical interface is still not very stable but it's working.
Just launch appKinter.pyw and enter your bulb ip then do whatever you want with it.
The graphical interface needs those modules : yeelight ; tkinter ; tkcolorpicker
