import math

##################################################
#                      _              /--\       #
#   -----       ----- | |            / /\_\      #
#  | |_||      | |_| || |--\        | |          #
#  | ---|__  __| ----|| |-| |__  __  \ \         #
#  ||    \ \/ /|_|    |_| |_|\ \/ / _ \ \        #
#         \  /                \  /  \\-| |       #
#         /_/                 /_/    \__/        #
#                                                #
##################################################

# VERSION 0.01

###
#   pyPhys is a simple physics engine simulating n body attracive (for now) physics.
#   The goal of this is to visualize the evolutionary dynamics of a system with many bodies.
#   Ideally, with many objects, a simple solar system would emerge with the right initial conditions. 
#
#   This is in the infant stages of development. 
#
#
#


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
"""
class Vector:
    def __init__(self):
        self.position = [0,0]
        self.vector = [0,0]

    def setPosition(self,x,y):
        self.position[0] = x
        self.position[1] = y

    def setVector(self,x,y):
        self.vector[0] =
        self.vector[1] = y
"""
### Mass is an astronomical body or particle, later allow for a charge, which may end up being a new 
###     property. .

class mass:
    def __init__(self,x,y,radius,timeStep):
        self.position = [x,y]
        self.mass = radius*2
        # radius size is in pixels
        self.radius = radius
        self.accelVector = [0,0]
        self.velocityVector = [0,0]
        self.timeStep = timeStep

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def getAccelVector(self):
        return self.accelVector

    def getVelocityVector(self):
        return self.velocityVector

    def getPosition(self):
        return self.position

    def setAccelVector(self,ax,ay):
        self.accelVector = [ax,ay]

    def setVelocityVector(self,vx,vy):
        self.velocityVector = [vx,vy]

    def setPosition(self,x,y):
        self.position = [x,y]

    def calculateVelocityVector(self):
        for index in range(0,len(self.accelVector)):
            self.velocityVector[index] = self.velocityVector[index] + self.accelVector[index]*self.timeStep

    def calculatePosition(self):
        for index in range(0,len(self.velocityVector)):
            self.position[index] = self.position[index] + self.velocityVector[index]*self.timeStep


    ##-----Collision Detection-----##


    def calculateDistMag(self,otherPosVect):
        x = self.position[0] - otherPosVect[0]
        y = self.position[1] - otherPosVect[1]

        return math.sqrt(x**2 + y**2)

    def calculateDistUnitVector(self,otherPosVect):

        mag = self.calculateDistMag(otherPosVect)

        delX = otherPosVect[0]-self.position[0]
        delY = otherPosVect[1]-self.position[1]

        distanceUnitVector = [delX/mag,delY/mag]

        return distanceUnitVector


        ##### TODO - Change this so it modifies both objects by 1/2 the separation distance.
        
    def isColliding(self,otherBody):

        otherPosVect = otherBody.getPosition()

        unitVect = self.calculateDistUnitVector(otherPosVect)
        separation = self.calculateDistMag(otherPosVect)

        desiredSeparation = self.radius + otherBody.radius

        if(separation < desiredSeparation):
            ## Take the position of self, and add self.radius+otherBody.radius magnitude to the unit Vector
            otherBody.setPosition(otherBody.getPosition()[0]+unitVect[0]*desiredSeparation/separation,
                             otherBody.getPosition()[1]+unitVect[1]*desiredSeparation/separation)

            #otherBody.setAccelVector(-self.getAccelVector()[0]/otherBody.getAccelVector()[0],-self.getAccelVector()[1]/otherBody.getAccelVector()[1])
            otherBody.setVelocityVector(-self.getVelocityVector()[0],-self.getVelocityVector()[1])

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
        #print("Mass1 position = {}".format(self.mass1.getPosition()))
        #print("Mass2 position = {}".format(self.mass2.getPosition()))
        x = self.mass2.getPosition()[0] - self.mass1.getPosition()[0]
        y = self.mass2.getPosition()[1] - self.mass1.getPosition()[1]

        self.distVector = [x,y]

    def calculateForce(self):
        self.calculateDistVector()
#        print("distVect = {}".format(self.distVector))
        r = self.calculateDistMag()

        #print("distMag = {}".format(r))
        forceVect = [0,0]
        for index in range(0,len(self.distVector)):
            forceVect[index] = ((self.gravConst*self.m)/(r**3))*self.distVector[index]

        #print("magnitude of Gravity = {}".format((self.gravConst*self.m)/((r)**3)))
#        print("mass = {}".format(self.m))
#        print("gravConst = {}".format(self.gravConst))
#        print("r**3 = {}".format((r)**3))
        #print("forceVect = {}".format(forceVect))
        return forceVect
