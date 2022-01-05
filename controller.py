import sys
from direct.actor.Actor import Actor
from direct.task import Task
from math import pi, sin, cos
import character
class playercontroller():
    player = None

    def __init__(self, show):
        self.player = character.Player(show)
        self.initmovement(show)

        


    def initmovement(self,showbase):
        showbase.accept('arrow_up',self.player.updateVelocity,[1,2,2])
        showbase.accept('shift-arrow_up',self.player.updateVelocity,[1,2,2])
        showbase.accept('arrow_up-up',self.player.updateVelocity,[-1,2,2])
        
        showbase.accept('arrow_down',self.player.updateVelocity,[-1,2,2])
        showbase.accept('shift-arrow_down',self.player.updateVelocity,[-1,2,2])
        showbase.accept('arrow_down-up',self.player.updateVelocity,[1,2,2])

        showbase.accept('arrow_left',self.player.updateVelocity,[2,-1,2])
        showbase.accept('shift-arrow_left',self.player.updateVelocity,[2,-1,2])
        showbase.accept('arrow_left-up',self.player.updateVelocity,[2,1,2])
        
        showbase.accept('arrow_right',self.player.updateVelocity,[2,1,2])
        showbase.accept('shift-arrow_right',self.player.updateVelocity,[2,1,2])
        showbase.accept('arrow_right-up',self.player.updateVelocity,[2,-1,2])

        showbase.accept(']',self.player.updateVelocity,[2,2,1])
        showbase.accept('shift-]',self.player.updateVelocity,[2,2,1])
        showbase.accept(']-up',self.player.updateVelocity,[2,2,-1])

        showbase.accept('[',self.player.updateVelocity,[2,2,-1])
        showbase.accept('shift-[',self.player.updateVelocity,[2,2,-1])
        showbase.accept('[-up',self.player.updateVelocity,[2,2,1])

        showbase.accept('lshift',self.player.toggle_sprint,[True])
        showbase.accept('lshift-up',self.player.toggle_sprint,[False])
        

        showbase.accept('escape',sys.exit)
