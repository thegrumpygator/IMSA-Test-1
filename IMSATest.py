# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:27:14 2016

@author: brian
"""

#import csv
import os

import numpy as np
import pandas as pd

verbose = True
verbose = False

print("numpy=%s; pandas=%s" % (np.__version__, pd.__version__))

pd.options.display.max_rows = 20
pd.options.display.width = 200

def main(name=strDataPath):
    # do stuff
    if not os.path.exists(name):
        print("Data does not exist at: ", name)
    
    # part 1 - load data as a DataFrame
    raw_df = load_data(name)
    
    if verbose:
        print("RAW df: ", raw_df)
    
    # Part 2 - reshape if necessary
    
def load_data(name):
    filename = name + "\\csv\\WeatherTech Championship Road Atlanta Race.csv"
    filename = name + "\\IWSC Daytona Race.csv"
    if verbose:
        print("Full file path: ", filename)
    
    #cols = 'Car Class Driver Lap LapTime SessionTime Flag Location S01 S02 S03 S04 S05 S06 S07 S08 SP4'
    #sep = '(?:(?<=[0-9])[.*] +)|(?:  +)'
    
    df = pd.read_csv(filename)
    
    if verbose:
        print("DF: ", df)
        print("Describe: ", df.describe())
        print("Columns: ", df.columns)
    
    #for col in df.columns:
    #    print("Col Type; ", col.type) # This line doesn't work
    return df


strDataPath = "N:\\Users\\brian\\Documents\\GitHub\\IMSA-Test-1\\Data\\2015-2016"
strDataPath = "IMSA-Test-1\\Data\\2015-2016"
strDataPath = "C:\\Users\\gator\\Documents\\IMSA-Test-1\\Data\\2015-2016"
strDataPath = "C:\\Users\\gator\\Documents\\IMSA-Test-1\\Data\\2017"

print("Main Data Path: ", strDataPath)
    
main(strDataPath)
