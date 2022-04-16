# Retrieve temperature data from https://www.ncdc.noaa.gov/cag/statewide/time-series

# original url = 'https://www.ncdc.noaa.gov/cag/statewide/time-series/1-tavg-1-2-1976-2022.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
# values within 'https://www.ncdc.noaa.gov/cag/statewide/time-series/<state>-tavg-1-<month>-1976-2022.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'

import requests
import csv

weather = {}

# sets up an empty weather dictionary
def initialize_dictionary():
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

    for year in range (1976, 2023):
        year_str = str(year)
        state_dict = {}
        for state in range (1, 51):
            state_name = num_to_state[state]
            state_dict[state_name] = {}

        weather[year_str] = state_dict

# downloads all the information into csv files
# WARNING: WILL TAKE APPROX 10 MINUTES
def download_all():
    str_start = 'https://www.ncdc.noaa.gov/cag/statewide/time-series/'
    str_middle = '-tavg-1-'
    str_end = '-1976-2022.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'

    # retrieves the information for every state
    for state in range(1, 51):
        # retrieves the information for every month
        for month in range(1, 13):
            # constructs the url where the csv file is stored
            url = (str_start + str(state) + str_middle + str(month) + str_end)
            # path for csv file (in the weather folder with name '<state>-<month>')
            placement = './weather_data/' + str(state) + '-' + str(month) + '.csv'

            # obtains the file and writes it to the designated path(placement)
            r = requests.get(url, allow_redirects=True)
            open(placement, 'wb').write(r.content)

    pass


# takes all the information out of the weather_data folder and puts it into a dictionary
    # Example of how to retrieve information
    # print(weather['2022']['Florida']['February'])
def upload_data():
    # goes through every state
    for state in range(1, 51):

        # goes through every month
        for month in range(1, 13):

            # gets path and opens file
            path = "./weather_data/" + str(state) + "-" + str(month) + ".csv"
            with open(path) as file:

                # reading the CSV file
                csv_file = csv.reader(file)

                cnt = 0
                for lines in csv_file:

                    # gets metadata from the first row
                    if cnt == 0:
                        state_str = lines[0]
                        month_str = lines[2][1:]

                    # starts getting numerical data
                    elif cnt > 4:
                        year_str = lines[0][:4]
                        obj = {
                            "value": lines[1],
                            "anomaly": lines[2]
                        }

                        # stores this data in the dictionary
                        weather[year_str][state_str][month_str] = obj

                    cnt = cnt + 1

    return weather
