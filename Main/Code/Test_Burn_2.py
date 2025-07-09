import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2 | 7-9-25", "Force.csv"))
Force = pd.read_csv(data_file)     # Read Force Data from Excel
F = Force.iloc[:,0].values 

order = 4
cutoff = 6 #Hz
F = func.LowPassFilter(F, cutoff, order)


script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2 | 7-9-25", "Pressure.csv"))
Pressure = pd.read_csv(data_file)     # Read Force Data from Excel
Pressure = Pressure.iloc[:,0].values 

order = 4
cutoff = 10
Pressure = func.LowPassFilter(Pressure, cutoff, order)


t = np.linspace(0,15,29999)


plt.plot(t,F)
plt.plot(t,Pressure)
plt.grid()
plt.show()

