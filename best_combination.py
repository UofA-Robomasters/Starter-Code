import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def cal_heat(v):
    return v ** 2

def cool_down(heat):
    heat = heat - COOL_SPEED / 50
    if heat < 0:
        heat = 0
    return heat

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

dmg_array = np.zeros((len(v_list), len(f_list)))
for v_index, v in enumerate(v_list):
# for v_index, v in enumerate(np.ones(36) * 25):
    for f_index, f in enumerate(f_list):
    # for f_index, f in enumerate(np.ones(49)*4):
        dmg = 0
        heat = 0
        counter = 0
        for t in np.linspace(0, 100, num=50*100, endpoint=False):   # 50Hz
            # print(t, counter, t > counter * 1.0 / f)
            if t > counter * 1.0 / f:
                if heat + cal_heat(v) < HEAT_LIMIT:
                    dmg += cal_dmg(v)
                    heat += cal_heat(v)
                    # print(t, heat, v, cal_dmg(v), dmg)
                counter += 1

            # print('before', heat)
            heat = cool_down(heat)
            # print(heat)
            # if t == 5:
            #     raise EOFError

        dmg_array[v_index][f_index] = dmg / 100
        # raise EOFError
# print(dmg_array)
fig = plt.figure()
ax = fig.gca(projection='3d')
v_list, f_list = np.meshgrid(f_list, v_list)
# surf = ax.plot_surface(v_list, f_list, dmg_array, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf = ax.plot_surface(v_list, f_list, dmg_array)
plt.show()
