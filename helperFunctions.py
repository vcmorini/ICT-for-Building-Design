# helper functions
import pandas as pd
from datetime import datetime
import numpy as np


#%% CONVERTING DATA FROM STRING TO DATETIME INDEX
# input: data
# output: data
def ind(data):
    time = []
    # for each index/row
    for i in range(len(data.index)):
        # reading  index
        t = data.index[i]
        # splitting day and hour
        day, hour = t.split('  ')
        # 
        timestamp = datetime.strptime(t, "%Y/%m/%d  %H:%M:%S")
        #
        time.append(timestamp)
    #
    data.index = pd.to_datetime(time)
    return data


#%% CONVERTING DATA TO FLOAT
# input: data
# output: data
def fl(data):
    # retrieving data columns
    cols = data.columns
    # for each columns
    for col in cols:
        # converting to float
        data[col] = data[col].astype(float)
    return data


#%% FITTING MISSING DATA
# input parameters: time series
# output parameters: fitted time series
def fitData(df):
    # fitting with zero, can also be done differently
    for i in np.arange(1,len(df.total_power) - 1):
        d1 = df.index[i]
        d2 = df.index[i+1]
        diff = d2.hour - d1.hour
        # EXPLORATION of the values we could have
        #print(diff)
        # if there is no missing values, go on
        if ((diff == 1) | (diff == -22) | (diff == 0)):
            pass
        # if there is a missing value
        else:
            # EXPLORATION
            #print("Inserting missing value")
            # to check if the initial and final size of df are given by missing hours
            for j in np.arange(diff):
                new = d1.replace(hour=d1.hour+j).strftime("%Y-%m-%d %H:%M:%S")
                df = df.append({'index':new,'total_power':df.total_power.mean(),'t_in':df.t_in.mean(),'t_out':df.t_out.mean(),'temp_diff':df.temp_diff.mean(),'power_heating':df.power_heating.mean(),'power_cooling':df.power_cooling.mean(),'power_electricity':df.power_electricity.mean()},ignore_index=True)
    return df
