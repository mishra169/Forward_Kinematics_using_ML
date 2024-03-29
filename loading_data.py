# -*- coding: utf-8 -*-
"""Loading_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h8UNZSHsaeqh5HGvrgGWIwgSr9YkVTiA
"""

import numpy as np
import pandas as pd

DATA = np.loadtxt("/content/robot_inverse_kinematics_dataset.csv", skiprows=1, delimiter=',')
print(DATA.shape)

#outputs are joint angles, we will split them separately
q_1 = DATA[:, 0]
q_2 = DATA[:, 1]
q_3 = DATA[:, 2]
q_4 = DATA[:, 3]
q_5 = DATA[:, 4]
q_6 = DATA[:, 5]

print("q1 shape: ", q_1.shape)
print("q2 shape: ", q_2.shape)
print("q3 shape: ", q_3.shape)
print("q4 shape: ", q_4.shape)
print("q5 shape: ", q_5.shape)
print("q6 shape: ", q_6.shape)

#inputs

x_ = DATA[:, 6]
y_ = DATA[:, 7]
z_ = DATA[:, 8]

print("x shape: ", x_.shape)
print("y shape: ", y_.shape)
print("z shape: ", z_.shape)

#reshaping data

print("\n\n\nReshaped Data\n")
q_1 = q_1.reshape(-1,1)
q_2 = q_2.reshape(-1,1)
q_3 = q_3.reshape(-1,1)
q_4 = q_4.reshape(-1,1)
q_5 = q_5.reshape(-1,1)
q_6 = q_6.reshape(-1,1)
x_ = x_.reshape(-1,1)
y_ = y_.reshape(-1,1)
z_ = z_.reshape(-1,1)
print("q1 reshaped: ", q_1.shape)
print("q2 reshaped: ", q_2.shape)
print("q3 reshaped: ", q_3.shape)
print("q4 reshaped: ", q_4.shape)
print("q5 reshaped: ", q_5.shape)
print("q6 reshaped: ", q_6.shape)
print("x reshaped: ", x_.shape)
print("y reshaped: ", y_.shape)
print("z reshaped: ", z_.shape)