"""Practice notebook Lesson #3
"""

#%%
import numpy as np 
import pandas as pd 


#%%
#Section 31 Question 1

w1 = np.array([2, 3, 5])
w2 = np.array([6, 5, 4])
b = np.array([-2, -2.2, -3])

def sigmoid(x):
    sigmoid = 1/(1 + np.exp(-x))
    return(sigmoid)

val_percep = w1*0.4 + w2*0.6 + b

sigmoid(val_percep)


# %%
