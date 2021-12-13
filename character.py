import sys
from direct.actor.Actor import Actor
from direct.task import Task
from math import pi, sin, cos
class Player():

    position = [0,0,0]
    deltaZ, deltaX, deltaY = 0,0,0
    pandaActor = None

    def __init__(self,showbase):
        '''This is called for the main character of the scene'''
        position = [0,0,0]#Sets position
        self.pandaActor = Actor("models/panda", {"walk":"models/panda-walk"})#Model and animations
        self.pandaActor.setScale(0.25, 0.25, 0.25)#Scale
        self.pandaActor.reparentTo(showbase.render)#ShowBase
        self.pandaActor.loop("walk")#Walk loop
        self.pandaActor.setHpr(0,0,0)
        self.spin = False

    def updateVelocity(self,directionX,directionZ,directionY):
        '''-1 is backwards, 1 is forwards, 0 is nomovement and 2 is don't change input'''
        
        if (directionX != 2):
            self.deltaX = self.deltaX + directionX
            
        if (directionY != 2):
            self.deltaY = self.deltaY + directionY
            
        if (directionZ != 2):
            self.deltaZ = self.deltaZ + directionZ
            
    def updatePosition(self,posX = None,posZ = None,posY = None):
        '''This updates the position based off of the given velocity or a given input'''
        if (posX == None and posZ == None and posY == None):
            self.position = [self.position[0] + 2 * self.deltaZ, self.position[1] + 2 * self.deltaX ,self.position[2] + 2 * self.deltaY]
        else:
            self.position = [posX,posZ,posY]
        #New position
        self.pandaActor.setPos(self.position[0],self.position[1],self.position[2])

    def handlemovement(self,showbase):
        #Does all of the showbase inputs just for cleanup
        showbase.accept('arrow_up',self.updateVelocity,[1,2,2])
        showbase.accept('arrow_up-up',self.updateVelocity,[-1,2,2])
        
        showbase.accept('arrow_down',self.updateVelocity,[-1,2,2])
        showbase.accept('arrow_down-up',self.updateVelocity,[1,2,2])

        showbase.accept('arrow_left',self.updateVelocity,[2,-1,2])
        showbase.accept('arrow_left-up',self.updateVelocity,[2,1,2])
        
        showbase.accept('arrow_right',self.updateVelocity,[2,1,2])
        showbase.accept('arrow_right-up',self.updateVelocity,[2,-1,2])

        showbase.accept(']',self.updateVelocity,[2,2,1])
        showbase.accept(']-up',self.updateVelocity,[2,2,-1])

        showbase.accept('[',self.updateVelocity,[2,2,-1])
        showbase.accept('[-up',self.updateVelocity,[2,2,1])

        showbase.accept('escape',sys.exit)

        showbase.accept('space',self.togglespin)

    def togglespin(self):
        self.spin = not self.spin

    def spinactor(self, task):
        if (self.spin):
            angleDegrees = task.time * 50.0
            angleRadians = angleDegrees * (pi / 180.0)
            self.pandaActor.setHpr(angleDegrees, 0, 0)
        return Task.cont