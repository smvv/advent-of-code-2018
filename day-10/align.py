import sys
import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

X = []
Y = []
dX = []
dY = []

for line in sys.stdin:
    parts = re.split('[<>,]', line)
    parts = list(map(int, [parts[1], parts[2], parts[4], parts[5]]))
    X.append(parts[0])
    Y.append(-parts[1])
    dX.append(parts[2])
    dY.append(-parts[3])

X = np.array(X)
Y = np.array(Y)
dX = np.array(dX)
dY = np.array(dY)

fig = plt.figure(1, figsize=(8, 8))

# Adjust the subplots region to leave some space for the slider.
fig.subplots_adjust(left=0.25, bottom=0.25)

ax = fig.add_subplot(111)
l, = ax.plot(X, Y, '.')

plt.xlim(-1000, 1000)
plt.ylim(-1000, 1000)

axt = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

t0 = 0
slider_time = Slider(axt, 't', 0, 20000, valinit=t0)


def press(event):
    if event.key in ['left', 'right']:
        change = 1 if event.key == 'right' else -1
        slider_time.set_val(slider_time.val + change)
        fig.canvas.draw_idle()


def update(val):
    t = slider_time.val
    l.set_xdata(X + int(t) * dX)
    l.set_ydata(Y + int(t) * dY)
    fig.canvas.draw_idle()


slider_time.on_changed(update)
fig.canvas.mpl_connect('key_press_event', press)

plt.show()
