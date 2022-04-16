# Calculate relevant statistics
# Useful resource: https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
from os import stat
from turtle import st
import temperatureretrieval as temperature
import statistics

# getting temperature data
temperature.initialize_dictionary()
weather = temperature.upload_data()

# Mean, Standard deviation, Covariance


# Mean of Weather by state for year: 
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
    11: "Hawaii",
    12: "Idaho",
    13: "Illinois",
    14: "Indiana",
    15: "Iowa",
    16: "Kansas",
    17: "Kentucky",
    18: "Louisiana",
    19: "Maine",
    20: "Maryland",
    21: "Massachusetts",
    22: "Michigan",
    23: "Minnesota",
    24: "Mississippi",
    25: "Missouri",
    26: "Montana",
    27: "Nebraska",
    28: "Nevada",
    29: "New Hampshire",
    30: "New Jersey",
    31: "New Mexico",
    32: "New York",
    33: "North Carolina",
    34: "North Dakota",
    35: "Ohio",
    36: "Oklahoma",
    37: "Oregon",
    38: "Pennsylvania",
    39: "Rhode Island",
    40: "South Carolina",
    41: "South Dakota",
    42: "Tennessee",
    43: "Texas",
    44: "Utah",
    45: "Vermont",
    46: "Virginia",
    47: "Washington",
    48: "West Virginia",
    49: "Wisconsin",
    50: "Wyoming",
    51: "District of Columbia",
    52: "American Samoa",
    53: "Guam",
    54: "Northern Mariana Islands",
    55: "Puerto Rico",
    56: "United States Minor Outlying Islands",
    57: "U.S. Virgin Islands",
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
means = {} 

for year in range (1976, 2023):
    state_dic = {}
    for state in range (1,51):
        temp = [0]
        state_dic[num_to_state[state]] = {}
        means[str(year)] = state_dic 
        
        for month in range (1,13):
            try:
                temp.append(float(weather[str(year)][num_to_state[state]][num_to_month[month]]['value']))
            except KeyError: #if no data is found for the state at the current month, set the value as 0 
                temp.append(0)
        
        obj = {
            'Mean' : statistics.mean(temp),
            'SD' : statistics.stdev(temp),
            'Variance' : statistics.variance(temp)
        }
        
        means[str(year)][num_to_state[state]] = obj
    
# Run Pearson's Correlation

# Run Spearman's Correlation