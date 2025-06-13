def QuickPlotData(x,y,xlabel,ylable,title):
# Quick Data plotting
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylable)
    plt.title(title)
    plt.grid()
    plt.show()


def LowPassFilter(Data, SamplingRate):
# Low Pass Filter (Butterworth)
    #cutoff_frequency = int(input("\n Choose cutoff frequency: ")) if u want to manually input cutoff freq
    cutoff_frequency = 20
    order = 4 # Order	 Result
              # 1–2	     Very smooth, may round off real signal
              # 4     	 Good balance: removes noise, keeps signal shape
              # 6	     Very sharp cutoff — good for very noisy data, may overshoot edges
    nyquist = SamplingRate / 2 # nyquist frequncy: max freq possible in signal without aliasing 
    normalized_cutoff = cutoff_frequency / nyquist

    b, a = butter(order, normalized_cutoff, btype='low')
    return filtfilt(b,a, Data)


def AeroTechData(): # create dictionary 
    # add these to README.md https://www.rocketmotorparts.com/75mm_Nozzle_0485__Throat/p1577809_20627885.aspx
                           #"https://aerotech-rocketry.com/products/product_3872d294-577c-353f-9773-6594597dfda3?_pos=2&_sid=036e31a62&_ss=r"
    g0 = 9.81 # m/s^2
    d_throat = 0.485 # diameter of throat (inches)
    A_star = np.pi * (d_throat / 2) ** 2 # Throat area, if choked flow, M = 1   
    d_exit = 1.250 # diameter of nozzle exit (inches)
    A_exit = np.pi * (d_exit / 2) ** 2 # Nozzle Exit Area
    Aerotech_Total_Impulse = 4603 # N-s (total impusle)
    Aerotech_Average_Thrust = 1420 # N
    Aerotech_Thrust_Duration = 3.2 # s
    Aerotech_Mass = 2560 / 1000 # kg
    Aerotech_Mass_Fow_Rate = Aerotech_Mass / Aerotech_Thrust_Duration  # Aertech mass flow rate based on provided vals   mass / burn time 
    Aerotech_Ve = Aerotech_Average_Thrust / Aerotech_Mass_Fow_Rate # F / mdot  gives m/s #https://www.grc.nasa.gov/www/k-12/airplane/specimp.html
    Aerotech_Specific_Impulse = Aerotech_Ve / g0 # (m/s) / (m/s^2)  # measure of how much thrust you get per unit of proppelant per second
    area_ratio = A_exit / A_star # area ratio calculation


def DataInformation(Data):
# this function takes a data file and calcs 
# (number of samples, sampling freq, dt, and t) 
    total_t = 15 # total time of data aquisition  # if data aquisition total time is changed this needs to be changed as well!
    
    print("\n--Imported Data Information--")
    num_samples = len(Data)  # total number of samples
    print(" Number of samples: " + str(num_samples))

    sampling_freq = num_samples/total_t  # samples/s  
    print("Sampling frequency: %.5g hz" % sampling_freq)

    dt = 1/sampling_freq # time between samples
    print("  Time per sample : %.3g s" % dt)
    t = np.arange(0,total_t, dt)
    print("-----------------------------")

    return num_samples, sampling_freq, dt, t







import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.optimize import fsolve 