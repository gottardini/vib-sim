from components import Wall,Mass,Spring,Damper,Forcing
from pylab import sign, cos, sin, pi, arange, sqrt, pi, array, array
from pylab import arange

setup=[["W1", Wall(position=0)],
       ["M1", Mass(mass=1,position=5,velocity=0)],
       ["M2", Mass(mass=1,position=13,velocity=0)],
       ["S1", Spring(stiffness=1,linkA="W1",linkB="M1",defLength=5)],
       ["S2", Spring(stiffness=1,linkA="M1",linkB="M2",defLength=5)],
       ["D1", Damper(dampingCoefficient=0.05,linkA="W1",linkB="M1")],
       ["D2", Damper(dampingCoefficient=0.05,linkA="M1",linkB="M2")],
       ["F1", Forcing(amplitude=0,omega=1,shift=0,link="M2")],
       ]
simSpan=(0,1000)
