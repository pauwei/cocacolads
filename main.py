from temperatureretrieval import *
from unemploymentretrieval import *
from testing import *
from fitting import *
import visualize as viz

#Example for getting unemployement data
#Best to load from pickle since there are query limits
# unemploymentData = getUnemploymentData(writeToFile=False, fromFile=True)
# print(unemploymentData['2000']['North Carolina'])

def main():
    #Get data for temperature and unemployment
    #Utilizes temperature retrieval and unemployment retrieval to pull data from online
    tempValues, unemployValues = testing.get_combined_list()

    #Calculate statistics
    mean_temp, mean_unemploy, sd_temp, sd_unemploy, cov, pearson, spearman = testing.calculate_stats(tempValues=tempValues, unemployValues=unemployValues)
    print(f'Mean Temperature: {mean_temp} \nMean Unemployment Rate: {mean_unemploy} \nSD Temperature: {sd_temp}\nSD Unemployment Rate: {sd_unemploy} \nCovariance: {cov}\nPearson\'s: {pearson} \nSpearman\'s: {spearman}')

    #Visualize the dataset
    pass

def testFunction():
    tempValues, unemployValues = testing.get_combined_list()
    viz.plotTempVsUnemploy(tempValues, unemployValues)
    #viz.plotTempVsUnemployByYear(tempValues, unemployValues)
    #viz.createGIFOverTime()
    viz.plotTempAndUnemployOverYear(tempValues, unemployValues)

if __name__ == '__main__':
    testFunction()
    #main()
