import math

class World:
    def __init__(self):

        #Size of window the world is in. This is in terms of pixels.

        self.bounds = [100,100]
        self.gravitationalConstant = 0
        self.masses = []

    def setBounds(self,width,height):
        self.bounds[0] = width
        self.bounds[1] = height

    def setGravitationalConstant(self,gravity):
        self.gravitationalConstant = gravity

    def getGravitationalConstant(self):
        return self.gravitationalConstant

    def addMass(self,mass):
        self.masses.append(mass)

### Generic Vector which an object can create to handle anything it wants.
class Vector:
    def __init__(self):
        self.position = [0,0]
        self.vector = [0,0]

    def setPosition(self,x,y):
        self.position[0] = x
        self.position[1] = y

    def setVector(self,x,y):
        self.vector[0] = x
        self.vector[1] = y

### Mass is an astronomical body or particle or later a charge.

class mass:
    def __init__(self,x,y,radius):
        self.position = [x,y]
        self.mass = radius*2
        # radius size is in pixels
        self.radius = radius
        self.accelVector = Vector()

    def getPosition(self):
        return self.position

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def setAccelVector(self,vector):
        self.accelVector = vector

#----------------------------#
# Use the formula            #
#   F = G*m1*m2*r/|r|^3      #
#----------------------------#
class Gravity:
    def __init__(self,mass1,mass2,gravConst):
        self.gravConst = gravConst
        self.mass1 = mass1
        self.mass2 = mass2
        self.m = mass2.getMass()
        self.accelVector = [0,0]
        self.distMag = 1; #Initialize to 1 so doesn't have any errant divide by 0
        self.distVector = [1,1]

    def calculateDistMag(self):
        x = self.distVector[0]
        y = self.distVector[1]

        return math.sqrt(x**2 + y**2)

    def calculateDistVector(self):
        print("Mass1 position = {}".format(self.mass1.getPosition()))
        print("Mass2 position = {}".format(self.mass2.getPosition()))
        x = self.mass2.getPosition()[0] - self.mass1.getPosition()[0]
        y = self.mass2.getPosition()[1] - self.mass1.getPosition()[1]

        self.distVector = [x,y]

    def calculateForceMag(self):
        self.calculateDistVector()
        print("distVect = {}".format(self.distVector))
        r = self.calculateDistMag()
        print("distMag = {}".format(r))
        forceVect = []
        for i in self.distVector:
            forceVect.append(((self.gravConst*self.m)/(r**3))*i)

        print("magnitude of Gravity = {}".format((self.gravConst*self.m)/((r)**3)))
        print("mass = {}".format(self.m))
        print("gravConst = {}".format(self.gravConst))
        print("r**3 = {}".format((r)**3))
        print("forceVect = {}".format(forceVect))

