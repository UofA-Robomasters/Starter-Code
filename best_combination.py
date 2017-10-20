import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def cal_heat(v):
    return v ** 2

def cool_down(heat):
    return heat - COOL_SPEED

def cal_dmg(v):
    if 10 <= v <= 25:
        return v ** 2
    else:
        # linear assumed, expected value returned
        prob_500 = 1 / (45 - 25) * (v - 25)
        return prob_500 * 500 + (1 - prob_500) * 50

HEAT_LIMIT = 1600
COOL_SPEED = 500

v_list = np.arange(10, 46)                       # m/s
f_list = np.linspace(0.1, 5, num=49)             # /s
# print(v_list)
# print(f_list)

dmg_array = np.zeros((len(v_list), len(f_list)))
for v_index, v in enumerate(v_list):
    for f_index, f in enumerate(f_list):
    # for f_index, f in enumerate(np.ones(49)*5):
        dmg = 0
        heat = 0
        last_time = 0
        if f > 1:
            iter_list = np.linspace(0, 100, num=f*100)
        else:
            iter_list = range(0, 100)
        for t in iter_list:
            # t_step
            for i in range(int(1//f)):
                # try shot
                if heat + cal_heat(v) < HEAT_LIMIT:
                    dmg += cal_dmg(v)
            if t % 1 == 0:
                heat = cool_down(heat)
            else:
                if math.ceil(t) > last_time:
                    # print("!")
                    heat = cool_down(heat)
                    last_time = t
        dmg_array[v_index][f_index] = dmg / 100
        # raise EOFError
# print(dmg_array)
fig = plt.figure()
ax = fig.gca(projection='3d')
v_list, f_list = np.meshgrid(f_list, v_list)
surf = ax.plot_surface(v_list, f_list, dmg_array, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
