# Based on calculated statistics find whether classification or regression is better

# Create model or regression line for prediction
import testing as testing
import matplotlib.pyplot as plt
import numpy as np 

def regression_plot():
    x,y = testing.get_combined_list()
    plt.scatter(x, y)
    b,a = np.polyfit(x,y, deg=1)
    xseq = np.linspace(0,10, num=100)
    plt.plot(xseq, a + b * xseq, color ='k')
    plt.show()

#Maybe check up on temperature vs unemployment for covid?
#Bucket temperature values to find possible higher mean?