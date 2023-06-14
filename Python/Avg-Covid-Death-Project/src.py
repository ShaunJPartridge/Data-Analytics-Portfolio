## Name: Shaun Partridge
## Course: CMPS-4553: Topics in Computational Science
## File: src.py
## Date: 9/23/2021
## Description: This program will open a csv file and extract the data from it to
## calculate and print the mean chance of someone dying from COVID-19 and the standard
## deviation of the mean.

import csv
import math
import numpy as np
from tabulate import tabulate
#from beautifultable import BeautifulTable
#from numpy.core.defchararray import isalpha, isnumeric


if __name__ == '__main__':

    # open file and read data
    with open("State_to_State_Migrations_Table_2019.csv") as infile:
        data = list(csv.reader(infile,delimiter=','))

    # this row or list has all of the state column headers
    state_col_headers = list(data[6]) 
    
    # get index of last column, which is 55
    totIndex = state_col_headers.index("Wyoming") 

    # each array or row in each sub-array is a column with a states' migration data
    XtoY = np.array([row[5:totIndex+1] for row in data[11:]])
    
    # Assign the transpose of the array to the array with blank elements removed
    XtoY = np.array([np.delete(row,-1) for row in XtoY.T[0:]])

    # cleaning up data here
    where_are_na = XtoY == 'N/A'
    XtoY[where_are_na] = 0

    # create the array for the final time and change the dtype to int
    XtoY = np.array([[el.replace(',','') for el in row] for row in XtoY],dtype=int)

    # create dictionary with state column headers as keys and each numpy array in XtoY as values
    simDict = dict(zip(state_col_headers[5:],XtoY))

    # create another dictionary to hold tuples of similar states as keys and the  
    # similarity scores between the two states as values
    myDict = {}

    # loop through simDicts' items
    for k,v in simDict.items():
        # loop through numpy array of XtoY values
        for i in range(len(v)):
            # if the XtoY value is bigger than the sum of the XtoY values divided by 50
            if v[i] > int(np.sum(v)/50):
                # Assign to a key, which is a tuple consisting of the current state and the state that's similar 
                # to it, the XtoY value
                myDict[(k,list(simDict.keys())[i])] = v[i]
     
    # get the 10 most similar pairs of states, by sorting dictionary 
    most_similar_states = sorted(myDict,key=myDict.get,reverse=True)[:10]
    
    # create table with tuples consisting of numbers 1-10 and tuples of paired similar states
    table = zip([i for i in range(1,11)],most_similar_states)

    # create a temp table to print to screen, since tabulate uses the table for the output file
    tmp_table = zip([i for i in range(1,11)],most_similar_states)

    # print table using module, tabulate
    print("The table below shows the 10 most similar pairs of states:\n\n",tabulate(tmp_table,headers=["Rank","Similar States"]))

    # write the output and table into a file
    with open("output.txt",'w') as of:
        of.write("The table below shows the 10 most similar pairs of states:\n\n")
        of.write(tabulate(table,headers=["Rank","Similar States"],tablefmt="grid"))
