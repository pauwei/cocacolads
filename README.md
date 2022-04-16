# Coca Cola Data Science Project

## Purpose

Demonstrate whether there is a correlation between weather and unmployment. Data ranges from 1976 to 2022, includes all 50 states, and divided by monthly units.

## Approach

### Retrieving Data

#### Retrieving Temperature Data - `temperatureretrieval.py`
	Input:
		start year: 1976
		end year: 2022
		state: [all]
		parameter: average temperature
		time scale: 1-Month
		month: [all]
	Output: 
		3d array [year (dict)][state (dict)][month (dict)]
			temperature object: value, rank, departure from mean
			example: sample_data['2000']['California']['January']

#### Retrieving Unemployment Data - `unemploymentretrieval.py`
    Input:
		start year: 1976
		end year: 2022
		Unemployment
	Output:
		3d array [year (dict)][state (dict)][month (dict)] => unmployment object
			unemployment object: unmployment rate, employment-population ratio
			example: sample_data['2000']['alabama']['jan']

### Testing - `testing.py`
    Data Statistics: mean, stdv, covariance
    Pearson's Correlation
    Spearman's Correlation

### Fitting - `fitting.py`
    If correlated, fit regression line

### Visualization - `visualize.py`
    Follow plots were created by year
        Temperature vs Unemployment Rate
		Temperature vs Unemployment Rate (1 year lag)
		Temperature vs Unemployment Rate (5 year lag)
		Temperature vs Unemployment Rate (10 year lag)
		Temperature vs Unemployment Rate (-1 year lag)
		Temperature vs Unemployment Rate (-5 year lag)
		Temperature vs Unemployment Rate (-10 year lag)

    Gif to visualize change over years by stitching plots

### Execution - `main.py`
    Functions are imported and executed

## Future work
    City temperature vs City CPI
		List of cities: New York, Philadelphia, Atlanta, Washington, Chicago, Los Angeles, San Francisco
