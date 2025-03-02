# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:38:19 2024

@author: kkadin
"""

import matplotlib.pyplot as plt
import math

# Filter type selection
# filter_type = "high_pass"  # Options: "low_pass", "high_pass"
filter_type = "low_pass"  # Options: "low_pass", "high_pass"

ZERO_COUNT = 10
zero_list = [0]*ZERO_COUNT

if filter_type == "low_pass": 
    ONE_COUNT = 100
elif filter_type == "high_pass":
    ONE_COUNT = 600
ones_list = [1]*ONE_COUNT

x_list = zero_list + ones_list
y_list = []

# Filter coefficients based on type
if filter_type == "low_pass":
    forget_factor = 0.1
    b = [forget_factor, 0]        # for input x
    a = [1, forget_factor-1]      # for output y
elif filter_type == "high_pass":
    b = [1, -1]                  # for input x
    a = [1, -0.99]               # for output y

y_nm1 = 0
x_nm1 = 0
for index, x_nm0 in enumerate(x_list, start=1):
    y_nm0 = (-a[1]*y_nm1 + b[0]*x_nm0 + b[1]*x_nm1)/a[0]
    y_list.append(y_nm0)
    y_nm1 = y_nm0
    x_nm1 = x_nm0

plt.plot(x_list)
plt.plot(y_list)

# find latency
latency_samples = 0
sample_rate = 60    # Hz

if filter_type == "low_pass":
    for index, y_nm0 in enumerate(y_list, start=1):
        if(y_nm0 > 0.90):   # 0.90 is 90% of the max value
            latency_samples = index
            break
elif filter_type == "high_pass":
    for index, y_nm0 in enumerate(y_list, start=1):
        if(index > ZERO_COUNT and y_nm0 < 0.1):  # 0.1 is 10% of the max value
            latency_samples = index
            break   

latency_ms = latency_samples*1/sample_rate*1000

plt.xlabel("samples")
if filter_type == "low_pass":
    plt.title("Low Pass Filter : Latency = {} samples ({:.0f} ms@{:.0f} Hz)".format(latency_samples, latency_ms, sample_rate))
elif filter_type == "high_pass":
    plt.title("High Pass Filter : Latency = {} samples ({:.0f} ms@{:.0f} Hz)".format(latency_samples, latency_ms, sample_rate))
    
plt.figtext(0.3, 0.5, "y(n) = (-{}*y(n-1) + {}*x(n) + {}*x(n-1))/{}".format(a[1],b[0],b[1],a[0]))


