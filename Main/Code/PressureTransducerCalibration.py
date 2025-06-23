import functions as func
import matplotlib.pyplot as plt
import numpy as np




_, _, _, _, PressureV  = func.GetCalibrationData()  # Voltage
_, _, _, t = func.DataInformation(PressureV, 30)

time_to_index = 30000 / 30   # 30000 samples / per 30 seconds

cutoff = 5
order = 4
PressureVFil = func.LowPassFilter(PressureV, cutoff, order )

# visually calculated steady state intervals
start = int(0 * time_to_index) 
end = int(17 * time_to_index)
PressureVFil = PressureVFil[start:end]
t = t[start:end]

start = int(0 * time_to_index) 
end = int(17 * time_to_index)
PressureV = PressureV[start:end]
t = t[start:end]

start = int(0 * time_to_index) 
end = int(7 * time_to_index)
vBase = PressureVFil[start:end]
tBase = t[start:end]

start = int(9.55 * time_to_index)
end = int(12.6 * time_to_index)
v100PSI = PressureVFil[start:end]
t100PSI = t[start:end]

baselineV = np.average(vBase)
onehundredpsiV = np.average(v100PSI)
######



#plt.plot(t, PressureV, label=f"Raw Pressure Reading")
plt.plot(t, PressureVFil, label=f"Filtered Pressure Reading", color='black')
plt.plot(tBase, vBase, label=f"Steady State 0 PSI: {baselineV:.4g} V", color='blue')
plt.plot(t100PSI, v100PSI, label=f"Steady State 100 PSI: {onehundredpsiV:.4g} V", color='red')
plt.title("Pressure Transducer calibration Data")
plt.legend()
plt.grid()
plt.show()

pressure_UP = 100
pressure_DOWN = 0

m = (pressure_UP - pressure_DOWN) / (onehundredpsiV - baselineV)    #  pressure (PSIG) / volt
b = -m * baselineV
