import requests
import json
import pickle

# Retrieve unmployment data from https://data.bls.gov/cgi-bin/surveymost?la
# API resource: https://www.bls.gov/developers/api_python.htm#python2

#Main function to get unemployment data
def getUnemploymentData(writeToFile=True, fromFile=False):
    #Returns data with like specifications: [year][state][month][type of data]
    #There are three types of data: UnmploymentRate, EmploymentPopulationRatio, LaborForceParticipationRate
    data = None

    #Read from pickle file or pull from website
    if fromFile:
        with open('unemploymentdata.pickle', 'rb') as handle:
            data = pickle.load(handle)
    else:
        data = requestUnemploymentData()
    
    #Write pulled results to file
    if not fromFile and writeToFile:
        with open('unemploymentdata.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return data

#Function that gets the data
def requestUnemploymentData():
    #Load the ids for the series data
    states, seriesID = getSeriesId()


    #Create and initialize 4D dictionary to store values
    unemploymentData = {}
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(1976, 2023):
        y = str(i)
        if i not in unemploymentData:
            unemploymentData[y] = {}

        for state in states.values():
            if state not in unemploymentData[y]:
                unemploymentData[y][state] = {}

            for month in months:
                if month not in unemploymentData[y][state]:
                    unemploymentData[y][state][month] = {}

                for sid in seriesID.values():
                    if sid not in unemploymentData[y][state][month]:
                        unemploymentData[y][state][month][sid] = "NA"

    #Year data ranges
    years = [(1976, 1995), (1996, 2015), (2015, 2022)]


    #Pull data by date ranges
    for year in years:

        for sid in seriesID:
            #Get series array parameters
            seriesArray = getSeriesArray(states, sid)


            #Make request for data
            headers = {'Content-type' : 'application/json'}
            data = json.dumps({"seriesid": seriesArray, "startyear":year[0], "endyear":year[1], "registrationkey":"c8da417fa87f4c0e813a8ad847cc85d9"})
            p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
            json_data = json.loads(p.text)

            print('Status: ', json_data['status'], '\nMessage: ', json_data['message'])

            if json_data['status'] != "REQUEST_SUCCEEDED":
                    print("Error in getting data for ", seriesArray, " from ", year[1], " to ", year[2], "\nError Code: ", json_data['status'])
                    return None

            for series in json_data['Results']['series']:
                state = states[series['seriesID'][5:7]]
                id = seriesID[series['seriesID'][7:]]
                for item in series['data']:
                    unemploymentData[item['year']][state][item['periodName']][id] = item['value']

    #Return data
    return unemploymentData

#Get an array of series id for request parameters
def getSeriesArray(states, seriesID):
    seriesArray = []

    for state in states:
        seriesArray.append("LAUST" + state + seriesID)

    return seriesArray

#Returns dictionary with series ids by state
def getSeriesId():
    states = {}

    states['01'] = 'Alabama'
    states['02'] = 'Alaska'
    states['04'] = 'Arizona'
    states['05'] = 'Arkansas'
    states['06'] = 'California'
    states['08'] = 'Colorado'
    states['09'] = 'Connecticut'
    states['10'] = 'Delaware'
    states['12'] = 'Florida'
    states['13'] = 'Georgia'
    states['15'] = 'Hawaii'
    states['16'] = 'Idaho'
    states['17'] = 'Illinois'
    states['18'] = 'Indiana'
    states['19'] = 'Iowa'
    states['20'] = 'Kansas'
    states['21'] = 'Kentucky'
    states['22'] = 'Louisiana'
    states['23'] = 'Maine'
    states['24'] = 'Maryland'
    states['25'] = 'Massachusetts'
    states['26'] = 'Michigan'
    states['27'] = 'Minnesota'
    states['28'] = 'Mississippi'
    states['29'] = 'Missouri'
    states['30'] = 'Montana'
    states['31'] = 'Nebraska'
    states['32'] = 'Nevada'
    states['33'] = 'New Hampshire'
    states['34'] = 'New Jersey'
    states['35'] = 'New Mexico'
    states['36'] = 'New York'
    states['37'] = 'North Carolina'
    states['38'] = 'North Dakota'
    states['39'] = 'Ohio'
    states['40'] = 'Oklahoma'
    states['41'] = 'Oregon'
    states['42'] = 'Pennsylvania'
    states['44'] = 'Rhode Island'
    states['45'] = 'South Carolina'
    states['46'] = 'South Dakota'
    states['47'] = 'Tennessee'
    states['48'] = 'Texas'
    states['49'] = 'Utah'
    states['50'] = 'Vermont'
    states['51'] = 'Virginia'
    states['53'] = 'Washington'
    states['54'] = 'West Virginia'
    states['55'] = 'Wisconsin'
    states['56'] = 'Wyoming'

    seriesID = {}
    seriesID['0000000000003'] = "UnemploymentRate"
    seriesID['0000000000007'] = "EmploymentPopulationRatio"
    seriesID['0000000000008'] = "LaborForceParticipationRate"

    return (states, seriesID)


def getSeriesDataByState(state, series, startyear, endyear):
    pass
