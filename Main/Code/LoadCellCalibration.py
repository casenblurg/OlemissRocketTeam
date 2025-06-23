import functions as func
import matplotlib.pyplot as plt
import numpy as np

two_kgV, BodyWeightV, LoadUnloadV, NoLoadV = func.GetCalibrationData()  # Voltage
_, _, forceV, _= func.GetBurnData()
_, _, _, t = func.DataInformation(two_kgV, 30)

cutoff = 1
order = 4

two_kgV = func.LowPassFilter(two_kgV, cutoff, order)
BodyWeightV = func.LowPassFilter(BodyWeightV, cutoff, order)
LoadUnloadV = func.LowPassFilter(LoadUnloadV, cutoff, order)
NoLoadV = func.LowPassFilter(NoLoadV, cutoff, order)

avg_NoLoadV = np.average(NoLoadV)
avg_2kgV = np.average(two_kgV)

#plt.plot(t,two_kgV,  label=f"2Kg Load; Average Reading: {avg_2kgV:.2g}")
#plt.plot(t, NoLoadV, label=f"No Load;  Average Reading: {avg_NoLoadV:.3g}")
#plt.title('Load Cell Calibration Plot')
#plt.xlabel("Time (s)")
#plt.ylabel("Voltage (V)")
#plt.grid()
#plt.legend()
#plt.show()

mass = 2 #kg

baseline_force = 0 # N
known_force = 2 * 9.80665 # N

baseline_V = avg_NoLoadV
known_V = avg_2kgV


m = (known_force - baseline_force) / (known_V - baseline_V)   #    force / volts      
b = -m * avg_NoLoadV     # bias 

force = (forceV * m) + b  # N
force *= 0.225

cutoff = 7
order = 4
force = func.LowPassFilter(force, cutoff, order)

ATtime = [0,  0.0386, 0.1236, 0.5023, 0.9969, 1.49923, 2.0016, 2.4807, 2.9212, 2.9907, 3.11443, 3.2400]
ATforce = np.array([0, 1332.26, 1563.48, 1519.44, 1574.49, 1662.58, 1574.49,
                   1409.34, 1299.23, 1167.11, 187.178, 0])
ATforce = 0.2248 * ATforce

percent_error = np.abs(np.max(force) - np.max(ATforce)) / np.max(ATforce) * 100
print(percent_error)
print(np.max(force))

plt.plot(t, force)
plt.plot(ATtime, ATforce)
plt.grid()
plt.show()




