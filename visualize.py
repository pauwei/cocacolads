# Plot data: see readme for additional information on how to plot

import glob
import imageio
import numpy as np
import matplotlib.pyplot as plt


def plotTempVsUnemploy(x, y):
    plt.title("Temperature vs Unemployment")
    plt.xlabel("Temperature in Fahrenheit")
    plt.ylabel("Unemployment Rate")

    plt.axis([-20, 100, 0, 35])
    plt.scatter(x, y)

    plt.savefig('./plots/TempVsUnemployAll.png')


def plotTempVsUnemployByYear(x, y):
    #Keep track of the year
    year = 1976

    #Data for one year should be a frame of 588
    for frameBegin in range(0, 27048, 588):
        
        plt.title("Temperature vs Unemployment in " + str(year))
        plt.xlabel("Temperature in Fahrenheit")
        plt.ylabel("Unemployment Rate")

        plt.axis([-20, 100, 0, 35])

        plt.scatter(x[frameBegin:frameBegin+588], y[frameBegin:frameBegin+588])
        
        filename = './plots/' + str(year) + '-TempVsUnemploy.png'
        plt.savefig(filename)

        year += 1

def plotTempAndUnemployOverYear(temp, unemploy):
    #Keep track of the year
    year = 1976

    #Variables
    x = []  #List of years
    y1 = [] #List of temperatures
    y2 = [] #List of unemployment

    #Data for one year should be a frame of 588
    for frameBegin in range(0, 27049, 588):
        x.append(year)

        y1.append(np.mean(temp[frameBegin:frameBegin+588]))
        y2.append(np.mean(unemploy[frameBegin:frameBegin+588]))

        year += 1

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.plot(x, y1, 'b-')
    ax2.plot(x, y2, 'r-')

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Temperature in Fahreinheit', color='b')
    ax2.set_ylabel('Average Unemployment Rate', color='r')

    plt.title("Temperature and Unemployment over Years")

    plt.savefig('./plots/TempAndUnemployOverYears.png')

def createGIFOverTime():
    #Get all filenames
    filenames = glob.glob('./plots/*.png')

    #Create gif using imageio
    with imageio.get_writer('./plots/AnimTempVsUnemploy.gif', mode='I', duration=0.5) as writer:
        for file in filenames:
            filename = file.replace('\\', '/')
            image = imageio.imread(filename)
            writer.append_data(image)
