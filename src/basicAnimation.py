import tkinter as tk
import time
import math

import random

#import Shapes

import Physics

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createMainCanvas()

    def createMainCanvas(self):
        self.screenHeight = 300
        self.screenWidth = 300
        self.canvas = tk.Canvas(self.master, width=self.screenWidth, height=self.screenHeight)

        self.canvas.pack()

        self.canvas.create_line(0,self.screenHeight-50,self.screenWidth,self.screenHeight-50)

        self.quit = tk.Button(self,text="QUIT", fg="red",
                              command=self.master.destroy)

        self.quit.pack(side="bottom")

    def createCircle(self,x,y,radius,canvasName):
        x0 = x-radius
        y0 = y-radius

        x1 = x+radius
        y1 = y+radius

        return canvasName.create_oval(x0,y0,x1,y1,fill='black')

    def Animate(self):

        world = Physics.World()
        world.setGravitationalConstant(2)

        mass1 = Physics.mass(30,150,30)

        mass2 = Physics.mass(270,150,30)

        self.createCircle(mass1.getPosition()[0],mass1.getPosition()[1],mass1.getRadius(),self.canvas)
        self.createCircle(mass2.getPosition()[0],mass2.getPosition()[1],mass2.getRadius(),self.canvas)

        grav = Physics.Gravity(mass1,mass2,world.getGravitationalConstant())

        grav.calculateForceMag()

root = tk.Tk()
app = Application(master=root)

app.Animate()
app.mainloop()


