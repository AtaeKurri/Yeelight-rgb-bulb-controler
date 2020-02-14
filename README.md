# Yeelight-rgb-bulb-controler
Command-line based app to control all of your yeelight rgb bulb
This program was made by Atae Kurri in 2020 using json and yeelight python libraries.
I don't own Yeelight.


# How to use

This program is command-line based, it means it has no graphical interface for the moment.
You can use multiple commands to control your rgb yeelight bulb.

To use your bulb in the program, in your yeelight or mihome application on your smartphone, please turn on remote control from local network. Overwise it'll not work at all and the bulb will not accept any commands from the program.

Then please use "addbulb <name> <ip of your bulb>" to add it to the config.json, or edit the file directly, then you can use the program.

- <bulb name> turn on/off
- <bulb name> pre <see config.json>
- <bulb name> brightness int
- <bulb name> rgb int int int
- addbulb <name> <ip>
- reloadconf (Warning : This command resets the content of the config.json, only do it if your config file is corrupted)
- backup (backups your config.json file into the same directory as the program)
  
There is an config.json filled with examples, feel free to delete or modify them to your liking.
But please, don't delete the config.json file or the program will no longer work


Please keep in mind using this program that i'm not an experienced programer, but I do my best, there is some errors that i can't seem to be able at the time to contain or explain in plain text. Keep in mind that the english translation is not perfect, being french.
