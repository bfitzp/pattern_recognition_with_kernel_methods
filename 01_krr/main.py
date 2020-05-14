# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:38:43 2020

@author: brian
"""
from compute_krr import compute_krr
from random import random
from random import sample

import math
import numpy as np
import sys
import time




sample_N = 250;         # No. of sample points
data_N = 100;           # No. of data points
noiseVar = 0.05;        # Noise variance

lam = 1e-4;           # Regularization
kernelType = 'Gauss'    # Kernel type
sigma = 1               # Kernel width

print('Hello World!')

start_time = time.time()

for x in range(1, 1000000):
    a = 1


x = np.array([6*(random()-0.5) for i in range(sample_N)])
noise = np.array([noiseVar*random() for i in range(sample_N)])

x_noise = np.sin(3*x)/x + noise

x_krr = np.linspace(-3, 3, data_N)


[alpha,y_2] = compute_krr(x,x_noise,kernelType,sigma,lam,x_krr)
y_krr = np.sin(3*x_krr)/x_krr

time_taken = time.time() - start_time;
print(f'{time_taken:.16f}')