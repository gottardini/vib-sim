class Wall:
    def __init__(self,position):
        self.position=position
        self.velocity=0

class Mass:
    def __init__(self,mass,position,velocity):
        self.mass=mass
        self.position=position
        self.velocity=velocity
        self.springs=[]
        self.dampers=[]
        self.forcings=[]

class Spring:
    def __init__(self,stiffness,linkA,linkB,defLength=0):
        self.stiffness=stiffness
        self.linkA=linkA
        self.linkB=linkB
        self.defLength=defLength

class Damper:
    def __init__(self,dampingCoefficient,linkA,linkB):
        self.dampingCoefficient=dampingCoefficient
        self.linkA=linkA
        self.linkB=linkB

class Forcing:
    def __init__(self,amplitude,omega,shift,link):
        self.amplitude=amplitude
        self.omega=omega
        self.shift=shift
        self.link=link
