import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import functions as func

known_pressure = 100 #PSIg

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData", "6-26-25", "PressureTransducerCalibraion_goodData.csv"))
pressure = pd.read_csv(data_file)     # Read Force Data from Excel
pressure = pressure.iloc[:,0].values 
pressureUnfiltered = pressure

order = 3
cutoff = 20

info = func.DataInformation(pressure,30)
t = info["t"]
pressure = func.LowPassFilter(pressure,cutoff,order)

time_to_index = 30000/30
start = int(5*time_to_index)
stop = int(25*time_to_index)

#Calibration Data
pressure = pressure[start:stop]
pressureUnfiltered = pressureUnfiltered[start:stop]
t = t[start:stop] - t[start]


# Ambient Data
start = 0 
stop = int(9.55*time_to_index)
steady_state_ambient = pressure[start:stop] 
steady_state_ambient_time = t[start:stop]

avg_ambientV = np.average(steady_state_ambient)


# 100 PSI Data
start = int(11.1*time_to_index)
stop = int(20*time_to_index)
steady_state_applied_pressure =  pressure[start:stop]
steady_state_applied_time = t[start:stop]

avg_appliedV = np.average(steady_state_applied_pressure)




plt.plot(t, pressureUnfiltered, label=f"Unfiltered Data",color='black')
plt.plot(t,pressure, label=f"Filtered Data: 20 Hz Low Pass")
plt.plot(steady_state_ambient_time,steady_state_ambient, label=f"Steady State Ambient Pressure: {avg_ambientV:0.3g} V")
plt.plot(steady_state_applied_time, steady_state_applied_pressure, label=f"Steady State 100 PSI: {avg_appliedV:0.3g} V")
plt.xlabel("Time (s)")
plt.ylabel("Pressure Transducer Voltage (V)")
plt.legend()
plt.title("PX309-3Kg10V Calibration")
plt.grid()
plt.plot()
plt.show()

