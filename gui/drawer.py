import pygame
import numpy as np
pygame.init()

massSize=(60,60)
wallSize=(5,60)
planePos=500
constK=1
springHeight=30

def drawPlane(screen):
    pygame.draw.line(screen, (0,0,0), [0, planePos], [1000, planePos], 5)

def drawWall(screen,pos):
    pygame.draw.rect(screen,(50,50,50),[pos-(wallSize[0]//2)+200,planePos-wallSize[1],wallSize[0],wallSize[1]],0)

def drawMass(screen,pos):
    pygame.draw.rect(screen, (100,100,100), [pos-(massSize[0]//2)+200, planePos-massSize[1], massSize[0], massSize[1]],0)
    pygame.draw.circle(screen, (0,0,0), [int(pos)+200, planePos-massSize[1]//2], 5, 0)

def drawSpring(screen, coords, l0, k):
    nPoints=l0*k*constK
    vec1,step=np.linspace(coords[0],coords[1],nPoints,retstep=True,endpoint=False)
    #print(vec1,step)
    vec1=np.add(vec1,step/4)
    vec2=np.add(vec1,step/2)
    vecX=np.ravel([vec1,vec2],"F")
    vecY = np.empty((nPoints*2,))
    vecY[::2] = 1
    vecY[1::2] = -1
    vecX=np.concatenate([[coords[0]],vecX,[coords[1]]])
    vecX=np.add(vecX,200)
    vecY=np.concatenate([[0],vecY,[0]])
    vecY=np.add(np.multiply(vecY,springHeight/2),planePos-massSize[1]/2)
    points=np.array((vecX,vecY)).T
    points=list(map(tuple, points))
    #print(points)

    pygame.draw.aalines(screen, (0,0,0), False, points)

    #pygame.draw.line(screen, (0,0,0), [coords[0]+200, planePos-massSize[1]//2], [coords[1]+200, planePos-massSize[1]//2], 2)
