# -*- coding: utf-8 -*-
"""EDA_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GCkEb7UtFV5WOLAPdUydrPGFe6PQkrdU
"""

import numpy as np
import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
import numpy as np
df=pd.read_csv('/content/robot_inverse_kinematics_dataset.csv')
df

#Printing data information
df.info

#Generating descriptive statistics of dataset
df.describe()

#Code to get the number of rows and columns
df.shape

#Code to find number of values in dataset
df.size

#Displaying first 5 rows
df.head()

#Displaying last 5 rows
df.tail()

df.isnull().sum()

df.corr()

#Plotting correlation heatmap
correlation_matrix =df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

#Code to fill null values
df['q5'].fillna(df['q5'].mean,inplace=True)
df['x'].fillna(df['x'].mean,inplace=True)
df['y'].fillna(df['y'].mean,inplace=True)
df['z'].fillna(df['z'].mean,inplace=True)

plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.title("Boxplot of Robot Dataset")
plt.show()

data = np.genfromtxt('/content/robot_inverse_kinematics_dataset.csv', delimiter=',', names=True, dtype=None, encoding=None)

x = data['x']
y = data['y']
z = data['z']
q1 = data['q1']
q2 = data['q2']
q3 = data['q3']
q4 = data['q4']
q5 = data['q5']
q6 = data['q6']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the end-effector path as a line
ax.plot(x, y, z, label='End-Effector Path', color='b')

# Customize the plot (you can adjust these settings as needed)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('6-DOF Robot End-Effector Path')

# Show the plot
ax.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(231)
plt.scatter(data['q1'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q1')
plt.ylabel('Y')
plt.title('Joint q1 vs. Y')

plt.subplot(232)
plt.scatter(data['q2'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q2')
plt.ylabel('Y')
plt.title('Joint q2 vs. Y')

plt.subplot(233)
plt.scatter(data['q3'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q3')
plt.ylabel('Y')
plt.title('Joint q3 vs. Y')

plt.subplot(234)
plt.scatter(data['q4'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q4')
plt.ylabel('Y')
plt.title('Joint q4 vs. Y')

plt.subplot(235)
plt.scatter(data['q5'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q5')
plt.ylabel('Y')
plt.title('Joint q5 vs. Y')

plt.subplot(236)
plt.scatter(data['q6'], data['y'], label='Y', alpha=0.5)
plt.xlabel('q6')
plt.ylabel('Y')
plt.title('Joint q6 vs. Y')

plt.tight_layout()
plt.show()

# Calculating errors between the calculated (x, y, z) and the actual (x, y, z)
calculated_x, calculated_y, calculated_z = data['x'], data['y'], data['z']
actual_x, actual_y, actual_z = data['q1'] * data['q2'], data['q2'] * data['q3'], data['q4'] * data['q5']

error_x = np.abs(calculated_x - actual_x)
error_y = np.abs(calculated_y - actual_y)
error_z = np.abs(calculated_z - actual_z)

# Plot errors
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.hist(error_x, bins=30, edgecolor='k')
plt.title("Error in X")
plt.subplot(132)
plt.hist(error_y, bins=30, edgecolor='k')
plt.title("Error in Y")
plt.subplot(133)
plt.hist(error_z, bins=30, edgecolor='k')
plt.title("Error in Z")
plt.show()

"""**DATA CORRECTION**"""

#Correcting the values showing more deflection from the mean

#FOR column q1
for x in df.index:
    if df.loc[x, "q1"] > -0.010:
        df.loc[x, "q1"] = df['q1'].mean()
    if df.loc[x, "q1"] < -0.090:
        df.loc[x, "q1"] = df['q1'].mean()

#FOR column q2
for x in df.index:
    if df.loc[x, "q2"] > 0.020:
        df.loc[x, "q2"] = df['q2'].mean()
    if df.loc[x, "q2"] < -0.050:
        df.loc[x, "q2"] = df['q2'].mean()

#FOR column q3
for x in df.index:
    if df.loc[x, "q3"] > 2.00:
        df.loc[x, "q3"] = df['q3'].mean()
    if df.loc[x, "q3"] < 1.00:
        df.loc[x, "q3"] = df['q3'].mean()

#FOR column q4
for x in df.index:
    if df.loc[x, "q4"] > 0.050:
        df.loc[x, "q4"] = df['q4'].mean()
    if df.loc[x, "q4"] < -0.030:
        df.loc[x, "q4"] = df['q4'].mean()

#For column q5
df['q5'] = pd.to_numeric(df['q5'], errors='coerce')  #To convert non-numeric values to numeric values
for x in df.index:
    if df.loc[x, "q5"] > 0.020:
        df.loc[x, "q5"] = df['q5'].mean()
    elif df.loc[x, "q5"] < -0.050:
        df.loc[x, "q5"] = df['q5'].mean()

#For column q6
for x in df.index:
    if df.loc[x, "q6"] > 3.60:
        df.loc[x, "q6"] = df['q6'].mean()
    elif df.loc[x, "q6"] < 2.80:
        df.loc[x, "q6"] = df['q6'].mean()

#FOR x
df['x'] = pd.to_numeric(df['x'], errors='coerce')   #To convert non-numeric values to numeric values
for x in df.index:
    if df.loc[x, "x"] > 20.90:
        df.loc[x, "x"] = df['x'].mean()
    if df.loc[x, "x"] < 18.90:
        df.loc[x, "x"] = df['x'].mean()

#FOR y
df['y'] = pd.to_numeric(df['y'], errors='coerce')   #To convert non-numeric values to numeric values
for x in df.index:
    if df.loc[x, "y"] > 0.008:
        df.loc[x, "y"] = df['y'].mean()
    if df.loc[x, "y"] < -0.001:
        df.loc[x, "y"] = df['y'].mean()

#FOR z
df['z'] = pd.to_numeric(df['z'], errors='coerce')   #To convert non-numeric values to numeric values
for x in df.index:
    if df.loc[x, "z"] > 90.504:
        df.loc[x, "z"] = df['z'].mean()
    if df.loc[x, "z"] < 88.504:
        df.loc[x, "z"] = df['z'].mean()

df