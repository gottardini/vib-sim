from config import setup,simSpan
from functions import validateSetup, findObj
import matplotlib.pylab as pylab
from scipy.integrate import odeint,solve_ivp
from pylab import plot,xlabel,ylabel,title,legend,figure,subplots
from pylab import sign, cos, sin, pi, arange, sqrt, pi, array, array
import sys
import gui

class sysSim:
    def __init__(self,objects,span):
        self.objects=objects
        self.timespan=span

    def integrator(self,t,state):
        #print(state)
        stateVec=[]
        counter=0
        for massName,massObj in self.objects["masses"].items():
            massObj.position=state[counter]
            massObj.velocity=state[counter+1]
            stateVec.append(massObj.velocity)
            acc=0
            for springConnection in massObj.springs:
                #print("Pos",massObj.position,findObj(self.objects,springConnection[0]).position)
                delta=massObj.position - findObj(self.objects,springConnection[0]).position
                acc-= sign(delta)*(sign(delta)*delta - springConnection[1].defLength)*springConnection[1].stiffness
                #print("Acc",acc)
            for damperConnection in massObj.dampers:
                acc-= (massObj.velocity - findObj(self.objects,damperConnection[0]).velocity)*damperConnection[1].dampingCoefficient
            for forcingConnection in massObj.forcings:
                acc+= forcingConnection.amplitude*sin(forcingConnection.omega*t-forcingConnection.shift)
            acc/=massObj.mass
            stateVec.append(acc)
            counter+=2
        return stateVec

    def start(self):
        startstate=[]
        for massName,massObj in self.objects["masses"].items():
            startstate.append(massObj.position)
            startstate.append(massObj.velocity)
        result = solve_ivp(self.integrator, self.timespan, startstate,max_step=0.1)
        return result




if __name__=="__main__":
    objects=validateSetup(setup)
    if objects:
        simulation=sysSim(objects,simSpan)
        UI=gui.UI()
        UI.prepare()
        result=simulation.start()
        print(result.t,result.y)
        counter=0
        for massName,massObj in simulation.objects["masses"].items():
            massObj.position=result.y[counter]
            massObj.velocity=result.y[counter+1]
            counter+=2

        UI.simulate(simulation.objects,result.t)
        #x = array(result.y[0])
        #xd = array(result.y[1])

        """
        # Plotting displacement and velocity
        pylab.rcParams['figure.figsize'] = (15, 12)
        pylab.rcParams['font.size'] = 18

        fig, ax1 = pylab.subplots()
        ax2 = ax1.twinx()
        ax1.plot(result.t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
        ax2.plot(result.t,xd,'g--',label = r'$\dot{x} (m/sec)$', linewidth=2.0)
        ax2.legend(loc='lower right')
        ax1.legend()
        ax1.set_xlabel('time , sec')
        ax1.set_ylabel('disp (mm)',color='b')
        ax2.set_ylabel('velocity (m/s)',color='g')

        pylab.grid()
        pylab.show()
        """
    else:
        print("\nInvalid setup\n")
        sys.exit()
