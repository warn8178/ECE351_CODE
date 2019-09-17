# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:48:25 2019

@author: katwa
"""

#######################################EXAMPLE 1####################################################

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14}) # set font size in plots

steps = 1e-2
t = np.arange(0,10+steps,steps) # to go up to 5.0, we must add a stepSize since `np.arange()` # goes up to (without including) the value of the second argument

print('# of elements: len(t) =',len(t), # notice this may be one larger than expected since `t` starts at 0
 '\nFirst element: t[0] =',t[0], # index the first value of the array `t`
 '\nLast element: t[len(t)-1] =',t[len(t)-1]) # index the last value of the array `t` 
            # Note that despite `t` having a length of 501, we index the 500th element since the first element is 0
            
#######################################EXAMPLE 2####################################################
# --- User-Defined Function --- #
# Create the output `y(t)` using a for loop and if/else statements

def example1(t):
 y = np.zeros((len(t),1)) # initialize `y` as a numpy array (of zeros)

 for i in range(len(t)):
     if i < (len(t)+1) / 3:
         y[i] = t[i]**2
     else:
             y[i] = np.sin(5*t[i]) + 2
 return y

#######################################EXAMPLE 3####################################################

y = example1(t) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('Background - Illustration of for Loops and if/else Statements')

t = np.arange(0,5+0.25,0.25)
y = example1(t)
plt.subplot(2,1,2)
plt.plot(t,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()

######################################Part 1##################################
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
steps = 1e-2
t = np.arange(0,2*3.14159+steps,steps)
def func1(t):
 x = np.zeros((len(t),1)) 

 for i in range(len(t)):
     x[i] = np.cos(t[i])
    
 return x


x = func1(t) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,x)
plt.grid(True)
plt.ylabel('x(t)')
plt.title('cos(t)')

#######################################Part 2#################################

###############Step Function################

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
steps = 1e-2

t = np.arange(-5,10+steps,steps)
def step(t):

 y = np.zeros((len(t),1)) 

 for i in range(len(t)):
     if t[i] >= 0:
         y[i] = 1
     else:
         y[i] = 0
 return y

y = step(t) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('Step function')

###############Ramp Function################

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
steps = 1e-2

t = np.arange(-5,10+steps,steps)
def ramp(t):

 y = np.zeros((len(t),1)) 

 for i in range(len(t)):
     if t[i] >= 0:
         y[i] = t[i]
     else:
         y[i] = 0
 return y

y = ramp(t) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,y)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('Ramp function')

################## User Defined #####################



t = np.arange(-5,10+steps,steps)
def user(t):

 y = np.zeros((len(t),1)) 
 
 y = ramp(t)-ramp(t-3)+5*step(t-3)-2*step(t-6)-2*ramp(t-6)
 return y

y = user(t)

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,y,"r")
plt.grid(True)
plt.ylabel('y(t)')
plt.title('User function')


#################### Time Reversal ##########################

y = 2*ramp(t)+2*step(t-3)-2*ramp(t-3)-5*step(t-6)-ramp(t-6)+ramp(t-9) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t,y,"r")
plt.grid(True)
plt.ylabel('y(t)')
plt.title(' Time Reversal')

###################### (t-4) ##################################

t = np.arange(0,12+steps,steps)

y = ramp(t-4)-ramp(t-4-3)+5*step(t-4-3)-2*step(t-4-6)-2*ramp(t-4-6) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t,y,"r")
plt.ylim(-3,10)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('(t-4)')

###################### (-t-4) ##################################

t = np.arange(-15,10+steps,steps)

y = ramp(-t-4)-ramp(-t-4-3)+5*step(-t-4-3)-2*step(-t-4-6)-2*ramp(-t-4-6) 

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t,y,"r")
plt.ylim(-3,10)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('(-t-4)')

###################### (t/2) ##################################

t = np.arange(0,15+steps,steps)

y = ramp((t/2))-ramp((t/2)-3)+5*step((t/2)-3)-2*step((t/2)-6)-2*ramp((t/2)-6)

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t,y,"r")
plt.ylim(-3,10)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('(t/2)')

###################### (2*t) ##################################

t = np.arange(0,7+steps,steps)

y = ramp((t*2))-ramp((t*2)-3)+5*step((t*2)-3)-2*step((t*2)-6)-2*ramp((t*2)-6) # initialize `y` as a numpy array (of zeros)

myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t,y,"r")
plt.ylim(-3,10)
plt.grid(True)
plt.ylabel('y(t)')
plt.title('2t')

###################### Derivative ##################################
steps = 1e-2
t = np.arange(0,10+steps,steps)
y = user(t) 
dt=np.diff(t)
dy= np.diff(y,axis=0)/dt


myFigSize = (10,8)
plt.figure(figsize=myFigSize)
plt.subplot(2,1,1)
plt.plot(t,user(t),':')
plt.plot(t[range(len(dy))],dy[:,0],"r",label='dy(t)/dt')
plt.grid(True)
plt.ylim([-5,10])
plt.ylabel('y(t)')
plt.title('Derivative')



























