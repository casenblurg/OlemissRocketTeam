print("functions.py is loaded")
print(__file__)


def voltsToLbs(DataInVolts):
    
    m, b = LCC.LoadCellCalibration()
    DataInVolts = np.array(DataInVolts)  # Ensure it's a NumPy array
    force = DataInVolts * m + b
    return force


def GetCalibrationData():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData", "6-23-25", "LoadCellCalibration_2KgLoad_623.csv"))
    Force = pd.read_csv(data_file)     # Read Force Data from Excel
    two_kg = Force.iloc[:,0].values 
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData", "6-23-25", "PressureTransducerCalibration_0to100PSI.csv"))
    Pressure = pd.read_csv(data_file)     # Read Force Data from Excel
    PressureCal = Pressure.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData",  "6-22-25", "LoadCellCalibration_BodyWeight.csv"))
    Force = pd.read_csv(data_file)     # Read Force Data from Excel
    BodyWeight = Force.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData", "6-22-25","LoadCellCalibration_Loading_Unloading_2Kg.csv"))
    Force = pd.read_csv(data_file)     # Read Force Data from Excel
    LoadUnload = Force.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "SensorCalibrationData",  "6-23-25", "LoadCellCalibration_0Load_623.csv"))
    Force = pd.read_csv(data_file)     # Read Force Data from Excel
    NoLoad = Force.iloc[:,0].values 




    return two_kg, BodyWeight, LoadUnload, NoLoad, PressureCal


def GetBurnData():
  
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 1 | 4-16-25", "Force.csv"))
    Force = pd.read_csv(data_file)     # Read Force Data from Excel
    F = Force.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 1 | 4-16-25", "Pressure.csv"))
    ChamberPressure = pd.read_csv(data_file) # Read Pressure Data from Excel
    Pc = ChamberPressure.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData", "Test Burn 1 | 4-16-25", "RawLoadCell.csv"))
    RawLoadCell = pd.read_csv(data_file)     # Read Force Data from Excel
    RawF = RawLoadCell.iloc[:,0].values 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData", "RawPressureTransducer.csv"))
    RawPressureTransducer = pd.read_csv(data_file) # Read Pressure Data from Excel
    RawP = RawPressureTransducer.iloc[:,0].values 

    return F, Pc, RawF, RawP



def QuickPlotData(x,y,xlabel,ylable,title):
# Quick Data plotting
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylable)
    plt.title(title)
    plt.grid()
    plt.show()


def PlotBurnData(F, Pc, RawF, RawP, filtered):


    if filtered == 0:
        
        #  Create a 2x2 grid of subplots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))


        # Plot Force (add annotation here only in top-left corner)
        axes[0, 0].plot(t, F)
        axes[0, 0].set_title("Force (lbf)")
        axes[0, 0].set_xlabel("Time (s)")
        axes[0, 0].set_ylabel("Force")
        axes[0, 0].grid(True)
        # Annotation in top-left
        axes[0, 0].text(
            0.02, 0.96,
            f"Samples: {num_samples+1:,}\nSampling Rate: {int(sampling_freq+1)} Hz",
            transform=axes[0, 0].transAxes,
            fontsize=9,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray')
        )


        # Plot Pressure
        axes[0, 1].plot(t, Pc)
        axes[0, 1].set_title("Chamber Pressure (PSI)")
        axes[0, 1].set_xlabel("Time (s)")
        axes[0, 1].set_ylabel("Pressure")
        axes[0, 1].grid(True)

        # Plot Raw Load Cell
        axes[1, 0].plot(t, RawF)
        axes[1, 0].set_title("Raw Load Cell (V)")
        axes[1, 0].set_xlabel("Time (s)")
        axes[1, 0].set_ylabel("Voltage")
        axes[1, 0].grid(True)

        # Plot Raw Pressure Transducer
        axes[1, 1].plot(t, RawP)
        axes[1, 1].set_title("Raw Pressure Transducer (V)")
        axes[1, 1].set_xlabel("Time (s)")
        axes[1, 1].set_ylabel("Voltage")
        axes[1, 1].grid(True)

        axes[0, 0].plot(t, F, color='k')  # red
        axes[0, 1].plot(t, Pc, color='b') # blue
        axes[1, 0].plot(t, RawF, color='k') # green
        axes[1, 1].plot(t, RawP, color='b') # black


        # Tight layout
        plt.tight_layout()
        plt.subplots_adjust(top=0.95, hspace=0.28)  # Add vertical spacing
        plt.show()

    elif filtered == 1:
       
        # Create a 1-row, 2-column grid of subplots
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # ---- Left Plot: Overlay 2 data sets ----
        axes[0].plot(t, RawF, label='Raw Force', color='black')
        axes[0].plot(t, F, label='Filtered Force', color='blue')
        axes[0].set_title("Thrust Comparison")
        axes[0].set_xlabel("Time (s)")
        axes[0].set_ylabel("Force (lbf)")
        axes[0].legend()
        axes[0].grid(True)

        # ---- Right Plot: Overlay 2 data sets ----
        axes[1].plot(t, RawP, label='Raw Pressure', color='black')
        axes[1].plot(t, Pc, label='Filtered Pressure', color='blue')
        axes[1].set_title("Chamber Pressure Comparison")
        axes[1].set_xlabel("Time (s)")
        axes[1].set_ylabel("Pressure (PSI)")
        axes[1].legend()
        axes[1].grid(True)

        # Layout
        plt.tight_layout()
        plt.show()



def LowPassFilter(Data, cutoff_frequency, order):
# Low Pass Filter (Butterworth)
    #cutoff_frequency = int(input("\n Choose cutoff frequency: ")) if u want to manually input cutoff freq
    #cutoff_frequency = 7 # could be changed for your cinvienience I just fouund that 7 hz works pretty well
    #order = 4 # Order	 Result
              # 1–2	     Very smooth, may round off real signal
              # 4     	 Good balance: removes noise, keeps signal shape
              # 6	     Very sharp cutoff — good for very noisy data, may overshoot edges
    
    sampling_freq = 2000
    nyquist = sampling_freq / 2 # nyquist frequncy: max freq possible in signal without aliasing 
    normalized_cutoff = cutoff_frequency / nyquist

    b, a = butter(order, normalized_cutoff, btype='low')
    return filtfilt(b,a, Data)


def AeroTechData(): # create dictionary 
    # add these to README.md https://www.rocketmotorparts.com/75mm_Nozzle_0485__Throat/p1577809_20627885.aspx
                           #"https://aerotech-rocketry.com/products/product_3872d294-577c-353f-9773-6594597dfda3?_pos=2&_sid=036e31a62&_ss=r"
    g0 = 9.81
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


def DataInformation(Data, total_t):
    global num_samples, sampling_freq, dt, t 
# this function takes a data file and calcs 
# (number of samples, sampling freq, dt, and t) 
    
    print("\n--Imported Data Information--")
    num_samples = len(Data)  # total number of samples
    print(" Number of samples: " + str(num_samples+1))

    sampling_freq = (num_samples)/total_t  # samples/s  
    print("Sampling frequency: " + str(round(sampling_freq)) + " hz" )

    dt = 1/sampling_freq # time between samples
    print("  Time per sample : %.3g s" % dt)
    t = np.arange(0,total_t, dt)
    print("-----------------------------")


    
    info = {"t":t, "num_samples":num_samples, "sampling_freq":sampling_freq, "dt":dt}
    return info 



import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import pandas as pd
import os
import LoadCellCalibration as LCC