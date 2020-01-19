import sys
sys.path.append("../")
# Import the pygame library and initialise the game engine
import pygame
pygame.init()

import gui.drawer
from functions import findObj
import numpy
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


class UI:
    def __init__(self,size=(1000,800)):
        # Open a new window
        self.size=size
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Mechanical Oscillator Sim")
        # The clock will be used to control how fast the screen updates
        self.clock = pygame.time.Clock()

    def prepare(self):
        self.screen.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Simulation in progress...', True, BLACK, WHITE)
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(text, textRect)
        pygame.display.flip()

    def simulate(self,objects,timeline):
        for t in range(0,len(timeline),1):
            print(t)
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                     pygame.quit() # Flag that we are done so we exit this loop
                     sys.exit()
            self.screen.fill(WHITE)
            drawer.drawPlane(self.screen)
            for wallName,wallObj in objects["walls"].items():
                drawer.drawWall(self.screen,wallObj.position*50)
            for massName,massObj in objects["masses"].items():
                drawer.drawMass(self.screen,massObj.position[t]*50)
            for springName,springObj in objects["springs"].items():
                posA=findObj(objects,springObj.linkA).position
                posB=findObj(objects,springObj.linkB).position
                #print("types",type(posA),type(posB))
                if type(posA)==numpy.ndarray:
                    posA=posA[t]
                if type(posB)==numpy.ndarray:
                    posB=posB[t]
                #print("Springpos",posA,posB)
                drawer.drawSpring(self.screen,(posA*50,posB*50),springObj.defLength,springObj.stiffness)
            pygame.display.flip()
            self.clock.tick(60)
