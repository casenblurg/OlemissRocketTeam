import functions as func
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

order = 4
cutoff = 7 # Hz

F, Pc, _, _ = func.GetBurnData()
_,_,_,t = func.DataInformation(F, 15)

F = func.LowPassFilter(F, cutoff, order)
Pc = func.LowPassFilter(Pc, cutoff, order)



# force vs time clean
newF = []
newTF = []

for i in range(len(F)):
    
    if F[i] > 0:
        newF.append(F[i])
        newTF.append(t[i])

newTF = newTF - newTF[0] 

burnTime = newTF[len(newTF) - 1] 
plt.plot(newTF, newF)
plt.title(f"Experimental Thrust vs Time (Burn Time: {burnTime:.2g} s) ")
plt.xlabel("Time (s)")
plt.ylabel("Force (lbf)")
plt.grid()
plt.show()



# pressure vs time clean
time_to_index = 30000 / 15

start = int(6.068 * time_to_index)
end = int(9.965 * time_to_index)

tPc = t[int(start):int(end)]
tPc = tPc - tPc[0]
Pc = Pc[int(start):int(end)]


plt.plot(tPc, Pc)
plt.title("Experimental Pressure vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (PSIG)")
plt.grid()
plt.show()


# compare burn thrust w aerotech thrust
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "..", "Documents", "AeroTech_L1420R_ThrustData.csv"))

df = pd.read_csv(data_file, skiprows=3)

AerotechTime = df['Time (s)'].values
AerotechThrust = 0.225 * df['Thrust (N)'].values

AerotechTime = np.insert(AerotechTime, 0, 0)       # Insert 0 at index 0
AerotechThrust = np.insert(AerotechThrust, 0, 0)   # Insert 0 at index 0

plt.plot(AerotechTime, AerotechThrust, label=f"Aerotech Thrust (Max F: {np.max(AerotechThrust):0.3g} lbf)")
plt.plot(newTF, newF, label=f"Test Thrust (Max F: {np.max(newF):0.3g} lbf)")
plt.title(f"Aerotech vs Test Burn ")
plt.xlabel("Time (s)")
plt.ylabel("Force (lbf)")
plt.legend()
plt.grid()
plt.show()




# Force vs Pressure both , individual



# calc burn time = 3.2s, peak thrust = 1646 N, total impulse = 4603 N-s, avg thrust = 1420 N