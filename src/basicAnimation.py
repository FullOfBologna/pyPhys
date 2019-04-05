import tkinter as tk
import time
import math

import random
import operator

#import Shapes

import Physics


class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createMainCanvas()

    def createMainCanvas(self):
        self.screenHeight = 600
        self.screenWidth = 600
        self.canvas = tk.Canvas(self.master, width=self.screenWidth, height=self.screenHeight)

        self.canvas.pack()

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
        #global circleObject

        world = Physics.World()
        world.setGravitationalConstant(1000)

        timeStep = 0.01

        massList = []
        massList.append(Physics.mass(290,300,10,timeStep*10))
        massList.append(Physics.mass(310,300,10,timeStep*10))
        massList.append(Physics.mass(540,300,1,timeStep*10))
        massList.append(Physics.mass(400,300,1,timeStep*10))

        massList[0].setVelocityVector(0,3.5)
        massList[1].setVelocityVector(0,-3.5)
        massList[2].setVelocityVector(0,-4)
        massList[3].setVelocityVector(0,-7)

        debugCounter = 0;


        while(True):

            accelVector = [0,0]

            #print("len(massList) = {}".format(len(massList)))

            for mass1 in massList:
                force = [0,0]
                for mass2 in massList:
                    if(mass1 != mass2):
                        grav = Physics.Gravity(mass1,mass2,world.getGravitationalConstant())
                        force = list(map(operator.add,force,grav.calculateForce()))

                for index in range(0,len(force)):
                    force[index] = force[index]/(len(massList)-1)
                    accelVector[index] = force[index]/mass1.getMass()

                mass1.setAccelVector(accelVector[0],accelVector[1])

            circleObject = []

            for mass in range(0,len(massList)):
                massList[mass].calculateVelocityVector()
                massList[mass].calculatePosition()
                circleObject.append(self.createCircle(massList[mass].getPosition()[0],massList[mass].getPosition()[1],massList[mass].getRadius(),self.canvas))

            #End while
            time.sleep(timeStep)
            debugCounter += 1
            self.master.update()

            for object in circleObject:
                self.canvas.delete(object)

            while(len(circleObject) > 0):
                del circleObject[0]




root = tk.Tk()
app = Application(master=root)

app.Animate()
app.mainloop()
