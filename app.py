# Python script for using yeelight rgb bulb.
# Made by Atae Kurri

#Version 1.0.1

from yeelight import Bulb
import json, jsonpickle, shutil

def main():
    with open("config.json", 'r') as config1:
        data1 = json.load(config1)
    try:
        commande = input("(help) > ")
        commande = commande.split(" ")


        if commande[0] == "addbulb":
            try:
                if commande[1]:
                    if commande[2:]:
                        data1["ips"][commande[1]] = str(commande[2])
                        with open("config.json", 'w') as config:
                            json.dump(data1, config, indent=2)
                        print("Done")
                        main()
            except Exception as error:
                print(f"[{error}]")
        elif commande[0] == "help":
            print("Please verify the spelling of the command.")
            print("""
- <bulb name> turn on/off
- <bulb name> pre <see config.json>
- <bulb name> brightness int
- <bulb name> rgb int int int
- addbulb <name> <ip>
- reloadconf
- backup""")
            main()
        elif commande[0] == "reloadconf":
            confirmation = input("Are you sure you want to reset your configuration file ? (Y/N) > ")
            if confirmation == "Y":
                data1 = {}
                data1["ips"] = {}
                data1["prereglage"] = {}
                data1["colors"] = {}
                with open("config.json", 'w') as config:
                    json.dump(data1, config, indent=2)
                print("Done.")
                main()
            else:
                main()
        elif commande[0] == "backup":
            shutil.copy("config.json", "config-backup.json")
            print("Done")
        elif commande[0] in data1["ips"]:
            bulb = Bulb(data1["ips"][commande[0]])
            if commande[1] == "turn":
                if commande[2] == "on":
                    bulb.turn_on()
                    print("Done")
                    main()
                if commande[2] == "off":
                    bulb.turn_off()
                    print("Done")
                    main()
            elif commande[1] == "brightness":
                brightness = int(commande[2])
                bulb.set_brightness(brightness)
                print("Done")
                main()
            elif commande[1] == "rgb":
                rgb1 = int(commande[2])
                rgb2 = int(commande[3])
                rgb3 = int(commande[4])
                bulb.set_rgb(rgb1, rgb2, rgb3)
                print("Done")
                main()
            elif commande[1] == "pre":
                option = commande[2]
                bulb.set_brightness(data1["prereglage"][option]["brightness"])
                bulb.set_rgb(data1["prereglage"][option]["rgb1"], data1["prereglage"][option]["rgb2"], data1["prereglage"][option]["rgb3"])
                print("Done")
                main()
            elif commande[1] == "color":
                option = commande[2]
                rgb = data1["colors"][option].split(",")
                print(f"{rgb[0]},{rgb[1]},{rgb[2]}")
                bulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))
                print("Done")
                main()
            else:
                print("Please verify the spelling of the command.")
                print("""
- <bulb name> turn on/off
- <bulb name> pre <see config.json>
- <bulb name> brightness int
- <bulb name> rgb int int int
- addbulb <name> <ip>
- reloadconf
- backup""")
                main()
        elif not commande[0]:
            print("Please type 'help' to see the list of commands.")
            main()
        else:
            print(f"You have no bulb named {commande[0]}")
            main()
    except Exception as error:
        print(f"The connection to your bulb has been reseted. Please restart the program. {error}")


if __name__ == '__main__':
    main()
