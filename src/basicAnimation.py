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

        timeStep = 0.1

        massList = []
        massList.append(Physics.mass(30,150,20,timeStep))
        massList.append(Physics.mass(270,150,30,timeStep))

        while(True):

            for mass1 in massList:
                force = [0,0]
                accelVector = [0,0]
                for mass2 in massList:
                    if(mass1 != mass2):
                        grav = Physics.Gravity(mass1,mass2,world.getGravitationalConstant())
                        force = force + grav.calculateForce()

                for index in range(0,len(force)):
                    force[index] = force[index]/(len(massList)-1)

                    accelVector[index] = force[index]/mass1.getMass()

                mass1.setAccelVector(accelVector)

            for mass in range(0,len(massList)):
                massList[mass].calculateVelocityVector()
                massList[mass].calculatePosition()

                self.createCircle(massList[mass].getPosition()[0],massList[mass].getPosition()[1],massList[mass].getRadius(),self.canvas)
            #End while


root = tk.Tk()
app = Application(master=root)

app.Animate()
app.mainloop()
