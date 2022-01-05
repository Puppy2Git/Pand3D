import sys
from direct.actor.Actor import Actor
from direct.task import Task
from math import pi, sin, cos
class Player():

    position = [0,0,0]
    deltaZ, deltaX, deltaY = 0,0,0
    pandaActor = None
    iswalking = False
    def __init__(self,showbase):
        '''This is called for the main character of the scene'''
        position = [0,0,0]#Sets position
        self.pandaActor = Actor("models/panda", {"walk":"models/panda-walk"})#Model and animations
        self.pandaActor.setScale(0.25, 0.25, 0.25)#Scale
        self.pandaActor.reparentTo(showbase.render)#ShowBase
        self.pandaActor.setPlayRate(1.50, "walk")
        self.sprint = False
        self.velocity = [0,0,0]
        self.pandaActor.setHpr(0,0,0)


    def updateVelocity(self,directionX,directionZ,directionY):
        '''-1 is backwards, 1 is forwards, 0 is nomovement and 2 is don't change input'''
        direction = 0
        
        zcalc = 1
        if (directionX != 2):
            if ((self.deltaX + directionX) >= 2 or (self.deltaX + directionX) <= -2):
                self.deltaX = self.deltaX
            else:
                self.deltaX = self.deltaX + directionX
                
            
        if (self.deltaX > 0):
            direction = direction + 180
            zcalc = -1/2
        elif (self.deltaX < 0):
            direction = direction - 0
            zcalc = 1/2
        
        if (directionY != 2):
            if ((self.deltaY + directionY) >= 2 or (self.deltaY + directionY) <= -2):
                self.deltaY = self.deltaY
            else:
                self.deltaY = self.deltaY + directionY
        
        if (directionZ != 2):
            if ((self.deltaZ + directionZ) >= 2 or (self.deltaZ + directionZ) <= -2):
                self.deltaZ = self.deltaZ
            else:
                self.deltaZ = self.deltaZ + directionZ

        if (self.deltaZ > 0):
            direction = direction + 90 * zcalc
        elif (self.deltaZ < 0):
            direction = direction - 90 * zcalc
        if (self.deltaX != 0 or self.deltaZ != 0):
            self.spinactor(direction)
            if (not self.iswalking):
                self.iswalking = True
                self.pandaActor.loop("walk")
                    
        else:
            if (self.iswalking):
                self.iswalking = False
                self.pandaActor.stop()
        self.velocity = [self.deltaX,self.deltaY,self.deltaZ]

        
            
    def updatePosition(self,posX = None,posZ = None,posY = None):
        '''This updates the position based off of the given velocity or a given input'''
        speed = 0.25
        speed = 0.50 if self.sprint == True else 0.25
        if (posX == None and posZ == None and posY == None):
            self.position = [self.position[0] + speed * self.deltaZ, self.position[1] + speed * self.deltaX ,self.position[2] + speed * self.deltaY]
        else:
            self.position = [posX,posZ,posY]
        #New position
        self.pandaActor.setPos(self.position[0],self.position[1],self.position[2])

    def toggle_sprint(self, val):
        if (val):
            self.pandaActor.setPlayRate(2.25, "walk")
        else:
            self.pandaActor.setPlayRate(1.50, "walk")
        self.sprint = val

    def spinactor(self, direction = 0):
        self.pandaActor.setHpr(direction, 0, 0)