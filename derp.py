#Imports using ShowBase
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.controls.PhysicsWalker import PhysicsWalker
import sys
import character
import controller

#The Main app class``
class mychar(PhysicsWalker):
    def __init__(self,show, path):
        super().__init__(gravity= -32.174, standableGround=0.707, hardLandingForce=16.0)
        self.initializeCollisions(collisionTraverser, path, wallBitmask, floorBitmask, avatarRadius=1.4, floorOffset=1.0, reach=1.0)
        self.enableAvatarControls()
        position = [0,0,0]#Sets position
        self.pandaActor = Actor("models/panda", {"walk":"models/panda-walk"})#Model and animations
        self.pandaActor.setScale(0.25, 0.25, 0.25)#Scale
        self.pandaActor.reparentTo(show.render)#ShowBase
        self.pandaActor.setPlayRate(1.50, "walk")
        #self.sprint = False
        #self.velocity = [0,0,0]
        self.pandaActor.setHpr(0,0,0)
    

class MyApp(ShowBase):
    

    def __init__(self):
        #inits ShowBase
        ShowBase.__init__(self)
        
        #Inits character and character movement
        
        #Loads the environment
        
        #Sets the camera position to Center
        self.position = [0,0,0]
        #Camera will be weird otherwise without disabling mouse
        #self.disable_mouse()

        
        self.scene = self.loader.loadModel("models/environment")
        self.newchar = mychar(self,self.scene)
        #Reparent the model to render.
        self.scene.reparentTo(self.render)
        #Apply Scale and position transforms on the model.
        self.scene.setScale(0.25,0.25,0.25)
        self.scene.setPos(-8,42,0)
        self.camera.setHpr(0,-10,0)
        #Adds the spinCameraTask procedure to the task manager

        
        
    #Spins camera that now does nothing
    

    

    
        


app = MyApp()
app.run()