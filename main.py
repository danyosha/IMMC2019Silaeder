from matplotlib import pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.set_aspect('equal')
plt.ion()

def onclick(event):
    if event.dblclick:
        fig, ax = plt.subplots()
        circle = plt.Circle((event.xdata,event.ydata),2.5,color='black')
        ax.set_xlim([-40, 40])
        ax.set_ylim([-40, 40])
        ax.set_aspect('equal')
        ax.add_artist(circle)
        plt.draw()

plt.show()
cid = fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()
