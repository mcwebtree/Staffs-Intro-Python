# display a chart of rainfall. 

# imports
import random as r
import matplotlib.pyplot as plt
import numpy as np
import pprint as pp

def create_chart( d_rain, f_inc_bar_labels = 0 ):
    fig, ax = plt.subplots()

    labels=[]
    data=[]

    for key, value in d_rain.items():
        labels.append( key )
        data.append( value )

    bars = ax.bar( labels, data , color='green', width=0.5)
   
    # set the x-axis to vertical text
    ax.set_xticks( range(12) )
    ax.set_xticklabels( labels , rotation=90 )

    # set the maximum value for the y-axis label
    max_value = (int( max( data.values() ) ) // 10 ) * 10
    ax.set_yticks(range(0, max_value + 10, 10))
    ax.set_yticklabels([str(i) for i in range(0, max_value + 10, 10)])

    ax.set_ylabel = "Rainfall (mm)"
    ax.set_title = "Rainfall by Month"

    if f_inc_bar_labels == 1:
        # add the value labels to the bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')
   
    plt.show()

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

## Generate test data for chart plotting practice. 
var_auto=input( "Do you want [A]utomatic or [M]anual values? ")
if var_auto.upper() == "A":
    d_rain = gen_rand_data( d_rain )
else:
    d_rain = get_actual_data ( d_rain )

var_labels=input( "Do you want the values displayed on the chart (Y/N)? ")

if var_labels.upper() == "Y":
    f_labels=1
else: 
    f_labels=0

create_chart ( d_rain , f_labels)

#
# Show the raw data. 
print ( "Chart created with this data: " )
pp.pprint ( d_rain, sort_dicts=False )
