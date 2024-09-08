# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:38:19 2024

@author: kkadi
"""

import matplotlib.pyplot as plt
import math

ZERO_COUNT = 10
ONE_COUNT = 60
ones_list = [1]*ONE_COUNT
zero_list = [0]*ZERO_COUNT
# item_count_list = list(range(0,ZERO_COUNT+ONE_COUNT))

x_nm0_list = zero_list + ones_list
# x_axis_tick_list = []

pi_value = math.pi

y_nm0 = 0
y_nm1 = 0
# forget_factor = 0.269
forget_factor = 0.0993
# forget_factor = 1- mathexp(-Ts/tau)
Fs = 60
Ts = 1/Fs
tau = -Ts/(math.log(1-forget_factor))
Fc = 1/(2*pi_value*tau)
y_nm0_list = []
y_nm1_list = []
for index, item in enumerate(x_nm0_list, start=1) :
    y_nm0 = ( 1-forget_factor)*y_nm1 + (forget_factor)*item
    y_nm0_list.append(y_nm0)
    y_nm1_list.append(y_nm1)
    y_nm1 = y_nm0
    # if(index < ZERO_COUNT):
    #     x_axis_tick_list.append(0)
    # else:
    #     x_axis_tick_list.append(16.77*(index-ZERO_COUNT))
            
# plt.plot(item_count_list, x_nm0_list)
# plt.plot(item_count_list, y_nm0_list)
# plt.plot(item_count_list, y_nm1_list)
plt.plot(x_nm0_list)
plt.plot(y_nm0_list)
# plt.plot(y_nm1_list)


# plt.xticks(ticks=item_count_list, labels=x_axis_tick_list)

# Optionally, you can label the x-axis
plt.xlabel("samples")
plt.title("r={:.3f}, tau={:.3f}[s], Fc={:.1f}[Hz]".format(forget_factor, tau, Fc))

# plt.text(len(data)/2, int(max), 'mean = {:.2f}, noise = {:.2f}, snr = {:.2f} '.format(mean, noise, snr), fontsize=12, color='red')

