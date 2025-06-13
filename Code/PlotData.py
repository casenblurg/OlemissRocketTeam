import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions 

F = pd.read_csv(r'C:/CaseyRocket/Data/Force.csv') # Load Cell Force Data     #add tkinter just open file system and select data
F = F.iloc[:,0].values  # iloc: = integer location based indexing
                        # iloc[:,0] means : select all rows, 0 selects the first column 
                        # .values converts panda series into np array

Pc = pd.read_csv(r'C:/CaseyRocket/Data/Pressure.csv') # Pressure Transducer (Dynamic Pressure aka chamber Pressure)
Pc = Pc.iloc[:,0].values  
num_samples, sampling_freq, dt, t = DataInformation(F) # See DataInformation()