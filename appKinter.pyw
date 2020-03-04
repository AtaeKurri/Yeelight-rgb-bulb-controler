# Python script for using yeelight rgb bulb.
# Made by Atae Kurri

#Version 1.0.0

from yeelight import Bulb
from tkinter import *
from tkcolorpicker import askcolor

class Main(Frame):
    def __init__(self, main, **kwargs):
        Frame.__init__(self, main, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.ipVar = StringVar()
        self.BrightVar = IntVar()
        self.ipVar.set("192.168.0.10")

        self.labelIP = Label(self, text="Enter the IP of your bulb.").pack()
        self.ipBox = Entry(self, width=15, textvariable=self.ipVar).pack()

        self.turnOnButton = Button(self, text='Turn On', fg="blue", command=self.TurnOn).pack()

        self.bouton_cliquer = Button(self, text="Turn Off", fg="blue", command=self.TurnOff).pack()

        self.button_rgb = Button(self, text="Set rgb color", fg="blue", command=self.selectRGB).pack()

        self.labelSale = Label(self, text="Select the Brightness level on the slider.").pack()
        self.brightnessScale = Scale(self, orient='horizontal', length=300, width=20, sliderlength=30, from_=1, to=100, tickinterval=100, variable=self.BrightVar).pack()
        self.brightnessButton = Button(self, text="Change brightness", fg="blue", command=self.setBrightness).pack()


    def TurnOn(self):
        ip = self.ipVar.get()
        Bulb(ip).turn_on()

    def TurnOff(self):
        ip = self.ipVar.get()
        Bulb(ip).turn_off()

    def selectRGB(self):
        rgb = askcolor(color="red", parent=None, title=("Color Chooser"), alpha=False)
        ip = self.ipVar.get()
        print(rgb[0])
        Bulb(ip).set_rgb(rgb[0][0], rgb[0][1], rgb[0][2])

    def setBrightness(self):
        ip = self.ipVar.get()
        brightnesslevel = self.BrightVar.get()
        Bulb(ip).set_brightness(brightnesslevel)

main = Tk()
main.title("Yeelight bulb controler")
interface = Main(main)

main.withdraw()
main.update_idletasks()
x = (main.winfo_screenwidth() - main.winfo_reqwidth()) / 2
y = (main.winfo_screenheight() - main.winfo_reqheight()) / 2
main.geometry("+%d+%d" % (x, y))
main.deiconify()
main.mainloop()

interface.mainloop()
interface.destroy()
