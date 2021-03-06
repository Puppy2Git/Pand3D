#Imports using ShowBase
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
import sys
import character
import controller

#The Main app class``
class MyApp(ShowBase):
    listtoupdate = []

    def __init__(self):
        #inits ShowBase
        ShowBase.__init__(self)

        #Inits character and character movement
        self.controller = controller.playercontroller(self)
        self.npc1 = character.Player(self)
        self.npc1.updateVelocity(1,2,2)
        self.npc2 = character.Player(self)
        self.npc2.updateVelocity(1,2,2)
        self.npc2.pandaActor.setPos(10,0,0)
        self.listtoupdate = [self.controller.player, self.npc1, self.npc2]
        #Loads the environment
        
        #Sets the camera position to Center
        self.position = [0,0,0]
        #Camera will be weird otherwise without disabling mouse
        self.disable_mouse()

        
        self.scene = self.loader.loadModel("models/environment")
        #Reparent the model to render.
        self.scene.reparentTo(self.render)
        #Apply Scale and position transforms on the model.
        self.scene.setScale(0.25,0.25,0.25)
        self.scene.setPos(-8,42,0)
        self.camera.setHpr(0,-10,0)
        #Adds the spinCameraTask procedure to the task manager

        self.taskMgr.add(self.movecamera, "update")
        
    #Spins camera that now does nothing
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    

    def movecamera(self, task):
        '''
        This is called in the task Manager to constantly update the camera's position
        '''
        
        #Update Position
        for acte in self.listtoupdate:
            acte.updatePosition()
        print(str(self.controller.player.position) + "                    ", end= "\r")
        #Camera offset
        offsetX = -30
        offsetY = 10
        #Sets camera Position
        self.camera.setPos(self.controller.player.position[0],self.controller.player.position[1] + offsetX,self.controller.player.position[2] + offsetY)
        
        return task.cont
        


app = MyApp()
app.run()