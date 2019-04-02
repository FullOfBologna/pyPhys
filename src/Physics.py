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
        self.gravitationalConstant = 0

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

    def getPosition(self):
        return self.position

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius


"""
class Gravity():
    def __init__(self):
        self.accelerationRate = 0;

    #-------------------------------------------------------#
    # accelerationRate will be in terms of pixel/timeStep^2 #
    #-------------------------------------------------------#
    def setGravity(self,accelerationRate):
        self.accelerationRate = accelerationRate

    def getGravity(self):
        return self.accelerationRate

class Velocity():
    def __init__(self):
        self.velocityVector = [0,0];

    #-------------------------------------------------------------------------#
    # Take the current velocity vector, and add the input accelerationVector
    #   -NOTE: accelerationVector must be the same size as velocity vector.
    #
    # This is an iterative calculation, so only perform one "time step"
    #-------------------------------------------------------------------------#

    def updateVelocity(self,accelerationVector):

        if len(accelerationVector) != len(self.velocityVector):
            return self.velocityVector

        for i in range(0,len(self.velocityVector)):
            self.velocityVector[i] = self.velocityVector[i] + accelerationVector[i]

        return self.velocityVector

    def setVelocityVector(self,inputVelocityVector):
        self.velocityVector = inputVelocityVector

    def getVelocityVector(self):
        return self.velocityVector

    def getSpeed(self):
        return math.sqrt(sum((x*100)**2 for x in self.velocityVector))
"""
