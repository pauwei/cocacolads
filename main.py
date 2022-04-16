<<<<<<< HEAD
from temperatureretrieval import *
from unemploymentretrieval import *
from testing import *
from fitting import *
from visualize import *
=======
from temperatureretrieval import *
from unemploymentretrieval import *
from testing import *
from fitting import *
from visualize import *

#Example for getting unemployement data
#Best to load from pickle since there are query limits
unemploymentData = getUnemploymentData(writeToFile=False, fromFile=True)
print(unemploymentData['2000']['North Carolina'])
>>>>>>> d7bbf50041db11452c4c5e324dd158b14bf4bbfc
