# Calculate relevant statistics
# Useful resource: https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
import temperatureretrieval as temperature
import unemploymentretrieval as unemploy
from scipy import stats
import numpy as np

# getting temperature data
temperature.initialize_dictionary()
weather = temperature.upload_data()
unemployment = unemploy.getUnemploymentData(writeToFile=False, fromFile=True)

# Mean, Standard deviation, Covariance

num_to_state = {
    1: "Alabama",
    2: "Alaska",
    3: "Arizona",
    4: "Arkansas",
    5: "California",
    6: "Colorado",
    7: "Connecticut",
    8: "Delaware",
    9: "Florida",
    10: "Georgia",
    11: "Idaho",
    12: "Illinois",
    13: "Indiana",
    14: "Iowa",
    15: "Kansas",
    16: "Kentucky",
    17: "Louisiana",
    18: "Maine",
    19: "Maryland",
    20: "Massachusetts",
    21: "Michigan",
    22: "Minnesota",
    23: "Mississippi",
    24: "Missouri",
    25: "Montana",
    26: "Nebraska",
    27: "Nevada",
    28: "New Hampshire",
    29: "New Jersey",
    30: "New Mexico",
    31: "New York",
    32: "North Carolina",
    33: "North Dakota",
    34: "Ohio",
    35: "Oklahoma",
    36: "Oregon",
    37: "Pennsylvania",
    38: "Rhode Island",
    39: "South Carolina",
    40: "South Dakota",
    41: "Tennessee",
    42: "Texas",
    43: "Utah",
    44: "Vermont",
    45: "Virginia",
    46: "Washington",
    47: "West Virginia",
    48: "Wisconsin",
    49: "Wyoming",
}

num_to_month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

# Finds the Mean, SD, and Var for the temperature data
def mean_by_months():
    tempValues = {} 
    unemployValues = {}

    for year in range (1976, 2022):
        state_dic = {}
        for state in range (1,50):
            weatherData = [0]
            unemployData = [0]
            state_dic[num_to_state[state]] = {}
            tempValues[str(year)] = state_dic 
            unemployValues[str(year)] = state_dic
            
            for month in range (1,13):
                weatherData.append(float(weather[str(year)][num_to_state[state]][num_to_month[month]]['value']))
                unemployData.append(float(unemployment[str(year)][num_to_state[state]][num_to_month[month]]['UnemploymentRate']))
            
            # calculates mean, sd, and var not including NaN Val
            tempObj = {
                'Mean' : np.nanmean(weatherData),
                'SD' : np.nanstd(weatherData),
                'Variance' : np.nanvar(weatherData)
            }
            
            unemployObj = {
                'Mean' : np.nanmean(unemployData),
                'SD' : np.nanstd(unemployData),
                'Variance' : np.nanvar(unemployData)
            }
            
            tempValues[str(year)][num_to_state[state]] = tempObj
            unemployValues[str(year)][num_to_state[state]] = unemployObj

def get_combined_list():
    tempValues = []
    unemployValues = []

    for year in range (1976, 2022):
        for state in range (1,50):
            for month in range (1,13):
                tempValues.append(float(weather[str(year)][num_to_state[state]][num_to_month[month]]['value']))
                unemployValues.append(float(unemployment[str(year)][num_to_state[state]][num_to_month[month]]['UnemploymentRate']))
    return tempValues, unemployValues

def calculate_stats(tempValues, unemployValues):
    tempValues, unemployValues = get_combined_list()
    mean_temp = np.mean(tempValues)
    mean_unemploy = np.mean(unemployValues)
    sd_temp = np.std(tempValues)
    sd_unemploy = np.std(unemployValues)
    combine_List = []
    combine_List.append(tempValues)
    combine_List.append(unemployValues)
        
    # Calulating Pearson's Correlation/Covariance/Spearman's Correlation
    cov = np.cov(combine_List)
    pearson = stats.pearsonr(tempValues, unemployValues)
    spearman = stats.spearmanr(tempValues, unemployValues)
    # print(f'Mean Temperature: {mean_temp} \nMean Unemployment Rate: {mean_unemploy} \nSD Temperature: {sd_temp}\nSD Unemployment Rate: {sd_unemploy} \nCovariance: {cov}\nPearson\'s: {pearson} \nSpearman\'s: {spearman}')
    return mean_temp, mean_unemploy, sd_temp, sd_unemploy, cov, pearson, spearman

