# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:27:14 2016

@author: brian
"""

import csv
import os

import numpy as np
import pandas as pd

print("numpy=%s; pandas=%s" % (np.__version__, pd.__version__))

pd.options.display.max_rows = 20
pd.options.display.width = 200

strDataPath = "N:\\Users\\brian\\Documents\\GitHub\\IMSA-Test-1\\Data\\2015-2016"

print(strDataPath)


def main(name=strDataPath):
    # do stuff
    if not os.path.exists(name):
        print("data does not exist at: ", name)
    
    # part 1 - load data as a DataFrame
    raw_df = load_data(name)
    
    # Part 2 - reshape if necessary
    
def load_data(name):
    filename = name + "\\csv\\WeatherTech Championship Road Atlanta Race.csv"
    print(filename)
    
    #cols = 'Car Class Driver Lap LapTime SessionTime Flag Location S01 S02 S03 S04 S05 S06 S07 S08 SP4'
    #sep = '(?:(?<=[0-9])[.*] +)|(?:  +)'
    
    df = pd.read_csv(filename)
    
    print(df)
    
    
main(strDataPath)
