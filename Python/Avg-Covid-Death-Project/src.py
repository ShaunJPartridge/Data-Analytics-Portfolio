## Name: Shaun Partridge
## Course: CMPS-4553: Topics in Computational Science
## File: src.py
## Date: 9/9/2021
## Description: This program will open a csv file and extract the data from it to
## calculate and print the mean chance of someone dying from COVID-19 and the standard
## deviation of the mean.

import csv
import math


if __name__ == '__main__':

    #open file and read data
    with open("CovidDeathCounts.csv") as infile:
        data = list(csv.reader(infile))
    #examine header fow to find column of interest
    ageIndex = data[0].index("Age")
    covidDeathsIndex = data[0].index("COVID-19 Deaths")
    
    #access field of interest in records and calculate/display stats
    ages = [int(row[ageIndex]) for row in data[1:] if row[ageIndex] != '']
    c_deaths = [int(row[covidDeathsIndex]) for row in data[1:] if row[covidDeathsIndex] != '']

    res = [float(int(row[ageIndex])* int(row[covidDeathsIndex])) for row in data[1:] if row[ageIndex] != '' and row[covidDeathsIndex] != '']
    
    freqs = sum(res)
    N = sum(c_deaths)
    mean = float(freqs/N)
    std = 0

    for i in range(len(ages)):
        std += (ages[i]-mean)**2
    std = math.sqrt(std/(N-1))
    
    with open('outfile.txt','w') as of:
        of.write("The average chance of someone dying from COVID-19 is: {}.\n".format(mean))
        of.write("The standard deviation of the mean is: {}.".format(std))

    print("The average chance of someone dying from COVID-19 is: {}.".format(mean))
    print("The standard deviation of the mean is: {}.".format(std))
