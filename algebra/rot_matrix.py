from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


theta=np.pi/2
u,v,w=1,1,1

fig=plt.figure(figsize=(10,10))
fig.suptitle(f'theta: {theta}, x: {u}, y: {v}, z: {w}',fontsize=16)

ax=fig.add_subplot(2,2,1)
a=np.array([u,v])
R=np.array([[np.cos(theta),-np.sin(theta)],
            [np.sin(theta),np.cos(theta)]])
b=R@a
V=np.array([a,b])
origin=[0],[0]
ax.quiver(*origin,V[:,0],V[:,1],color=['r','b'],scale=5)
ax.title.set_text('2d rotation')

ax=fig.add_subplot(2,2,2,projection='3d')
x,y,z=np.meshgrid(np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1))
a=np.array([u,v,w])
Rx=np.array([[1,0,0],
            [0,np.cos(theta),-np.sin(theta)],
            [0,np.sin(theta),np.cos(theta)]])
b=Rx@a
V=np.array([a,b])
origin=[0],[0],[0]
ax.quiver(*origin,V[:,0],V[:,1],V[:,2],color=['r','b'],length=0.05,normalize=True)
ax.title.set_text('3d rotation around x')

ax=fig.add_subplot(2,2,3,projection='3d')
x,y,z=np.meshgrid(np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1))
a=np.array([u,v,w])
Ry=np.array([[np.cos(theta),0,np.sin(theta)],
             [0,1,0],
             [-np.sin(theta),0,np.cos(theta)]])
b=Ry@a
V=np.array([a,b])
origin=[0],[0],[0]
ax.quiver(*origin,V[:,0],V[:,1],V[:,2],color=['r','b'],length=0.05,normalize=True)
ax.title.set_text('3d rotation around y')

ax=fig.add_subplot(2,2,4,projection='3d')
x,y,z=np.meshgrid(np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1),
                  np.arange(-5,5,0.1))
a=np.array([u,v,w])
Rz=np.array([[np.cos(theta),-np.sin(theta),0],
             [np.sin(theta),np.cos(theta),0],
             [0,0,1]])
b=Rz@a
V=np.array([a,b])
origin=[0],[0],[0]
ax.quiver(*origin,V[:,0],V[:,1],V[:,2],color=['r','b'],length=0.05,normalize=True)
ax.title.set_text('3d rotation around z')

plt.subplots_adjust(hspace=0.5)

plt.show()
