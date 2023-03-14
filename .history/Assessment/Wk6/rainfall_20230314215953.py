# display a chart of rainfall. 

# imports
import random as r
import matplotlib.pyplot as plt
import numpy as np

def create_chart():
    return 1

def gen_rand_data(d_rain):
    for key, value in d_rain.items():
        d_rain[key]=r.randrange(0,80)
    return d_rain

def get_actual_data( d_rain ):
    for key, value in d_rain.items():
        d_rain[key]=int( input( f'Please enter the rainfall for {key}: ' ) )
    return d_rain

d_rain = {"January": 0, 
          "February": 0, 
          "March": 0,
          "April": 0,
          "May": 0,
          "June": 0,
          "July": 0,
          "August": 0,
          "September": 0,
          "October": 0,
          "November": 0,
          "December": 0 }

d_rain = gen_rand_data( d_rain )

