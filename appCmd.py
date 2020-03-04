# Python script for using yeelight rgb bulb.
# Made by Atae Kurri

#Version 1.0.2

from yeelight import Bulb
import json, argparse

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("ip", type=str, help="Tells the program what bulb to control.")
    parse.add_argument("-t", "--turn", help="trigger the power state.", choices=["on", "off"])
    parse.add_argument("-b", "--brightness", type=int, help="Set the brightness to a value.")
    parse.add_argument("-c", "--rgb", type=int, help="Set a color from the rgb format.", nargs=3)
    args = parse.parse_args()
    bulb = Bulb(args.ip)

    try:
        if args.turn == "on":
            turnOn(bulb)
        elif args.turn == "off":
            turnOff(bulb)
        else:
            pass
        if args.brightness:
            brightness(bulb, args.brightness)
        if args.rgb:
            rgb(bulb, args.rgb)
    except Exception as error:
        print(f"The bulb's ip is not correct. {error}")


def turnOn(bulb):
    bulb.turn_on()

def turnOff(bulb):
    bulb.turn_off()

def brightness(bulb, value):
    bulb.set_brightness(value)

def rgb(bulb, value):
    bulb.set_rgb(value[0], value[1], value[2])

if __name__ == '__main__':
    main()
