import functions as func
import matplotlib.pyplot as plt
import numpy as np



def LoadCellCalibration():

    two_kgV, _, _, NoLoadV, _ = func.GetCalibrationData()  # Voltage
    _, _, _, t = func.DataInformation(two_kgV, 30)

    time_to_index = 30000 / 30   # 30000 samples / per 30 seconds

    start = int(15 * time_to_index)
    end = 29999

    two_kgV = two_kgV[int(start):int(end)+1]
    t = t[int(start):int(end)+1]
    NoLoadV = NoLoadV[start:end+1]

    cutoff = 1
    order = 4

    two_kgV = func.LowPassFilter(two_kgV, cutoff, order)
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


    m = 0.225 * (known_force - baseline_force) / (known_V - baseline_V)   #    force (lbs) / volt      
    b = -m * avg_NoLoadV     # bias 

    print (f"The Loadcell output is lbf = {m:.7g} lbs/V + {b:.4g} lbs")

    return m, b






