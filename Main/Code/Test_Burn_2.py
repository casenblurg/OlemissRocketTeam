import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 
import os
import LoadCellCalibration as Lcal

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2", "RawLoadCell_Test2.csv"))
F_voltage = pd.read_csv(data_file)     # Read Force Data from Excel
F_voltage = F_voltage.iloc[:,0].values 

m,b = Lcal.LoadCellCalibration()
Force = (F_voltage * m) + b


order = 4
cutoff = 5
Force = func.LowPassFilter(Force, cutoff, order)


script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2", "Pressure_Test2.csv"))
Pressure = pd.read_csv(data_file)     # Read Force Data from Excel
Pressure = Pressure.iloc[:,0].values 

order = 4
cutoff = 10
Pressure = func.LowPassFilter(Pressure, cutoff, order)


time = np.linspace(0,15,29999)


plt.plot(time, Force)
plt.grid()
plt.show()


