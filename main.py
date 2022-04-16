from temperatureretrieval import *
from unemploymentretrieval import *
from testing import *
from fitting import *
from visualize import *

#Example for getting unemployement data
#Best to load from pickle since there are query limits
unemploymentData = getUnemploymentData(writeToFile=False, fromFile=True)
print(unemploymentData['2000']['North Carolina'])