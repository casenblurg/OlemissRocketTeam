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


def PlotData(x,y,xlabel,ylable,title):
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
              # 6	     Very sharp cutoff — good for very noisy data, but may "ring" or overshoot edges
    nyquist = SamplingRate / 2 # nyquist frequncy: max freq possible in signal without aliasing 
    normalized_cutoff = cutoff_frequency / nyquist

    b, a = butter(order, normalized_cutoff, btype='low')
    return filtfilt(b,a, Data)


def CalcStartStopBurn (Force, time, SamplingRate, Aerotech_Thrust_Duration):
# this function calculates the start burn and stop burn and graphs it assuming the load cell was not zeroed before burn. 
# your data set should start less than zero if using this func
# func can also return calculated burn time   # also need to make a better way to calc burn time more accurately 
    count1 = 0
    count2 = 0
    start = 0
    stop = 0
    for i in range(len(Force)):

        if Force[i] > 0 and count1 == 0:
            count1 += 1
            start = i

        if i > 15000 and Force[i] < 0:
            count2 += 1
            if count2 == 2:
                stop = i
    
    newF = Force[start:stop]
    BurnForce = newF * 4.448 # force array in N

    newt = time[start:stop]
    newt = newt - time[start]
    percent_error = abs( (((len(newt)/SamplingRate)) - Aerotech_Thrust_Duration) / Aerotech_Thrust_Duration) * 100
   
    print("\n-------Burn Time------------")
    print("  Calculated Burn Time: %.2f" % (len(newt) / SamplingRate) + " s")
    print("   Aerotech Burn Time : %.2f" % Aerotech_Thrust_Duration + " s")
    print("      Percent Error   : %.3g" % percent_error +" %")
    print("-----------------------------")

    #PlotData(newt, newF, "Time (s)", "Force(lbs)", "(Actual Burn) Force vs. Time")  #Uncomment this line to graph it
    return len(newt) / SamplingRate , BurnForce


def ExitMach(AreaRatio, gamma):
# This function calculates the exit mach number based on the calculated area ratio and gamma (1.2)
# you can use nasa's calculator "https://www.grc.nasa.gov/www/k-12/airplane/astar.html" or estimate using "https://engineering.purdue.edu/~propulsi/propulsion/flow/isent12.html"
    def equation(Me):
        left = AreaRatio
        right = (1 / Me) * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * Me**2))**((gamma + 1)/(2 * (gamma - 1)))
        return left - right

    Me_guess = 2.5
    Me = fsolve(equation, Me_guess)[0]
    return Me


def CalcultateMassFlowRate (MotorMass, CalculatedBurnTime, Aerotech_Mass_Flowrate):
# this func estimates mass flow rate based on provided data
# uses aerotech provided mass and calculated burn time of actual test
    mdot = MotorMass / CalculatedBurnTime
    percent_error = (abs(mdot - Aerotech_Mass_Flowrate) / Aerotech_Mass_Flowrate) * 100 
    print("\n-----Mass Flow Rate---------")
    print("Calculated Mass Flow Rate: %.3g" % mdot + " kg/s")
    print(" Aerotech Mass Flow Rate : %.3f" % Aerotech_Mass_Flowrate + " kg/s")
    print("      Percent Error      : %.2f" % percent_error +" %")
    print("-----------------------------")

    return mdot


def CalculateExitVelocity (BurnForce, CalculatedMassFlowRate, Aerotech_Ve):  # Force should be in N    CalcMassFLowRate should be in kg/s 
    avgForce = np.average(BurnForce)
    calculated_Ve = avgForce / CalculatedMassFlowRate
    percent_error_Ve = abs((calculated_Ve - Aerotech_Ve) / Aerotech_Ve) * 100

    print("\n------Exit Velocity---------")
    print("  Calculated Ve : %.2f" % calculated_Ve + " m/s")
    print("   Aerotech Ve  : %.2f" % Aerotech_Ve + " m/s")
    print("  Percent Error : %.2f" % percent_error_Ve + " %")
    print("-----------------------------")

    return calculated_Ve # m/s


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.optimize import fsolve 



# Constants
g0 = 9.81 # m/s
gamma = 1.2 # common gamma for SRM's

def main():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # this code is for the analysis of the data obtained from static fire tests of
    # "AeroTech L1420R-PS RMS-75/5120 Reload Kit (1 Pack) - 12142P" conducted by the OleMissRocketTeam

    # Known Paramaters and Provided Values from Aerotech: https://www.rocketmotorparts.com/75mm_Nozzle_0485__Throat/p1577809_20627885.aspx
                                                          #"https://aerotech-rocketry.com/products/product_3872d294-577c-353f-9773-6594597dfda3?_pos=2&_sid=036e31a62&_ss=r"
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
    Me = ExitMach(area_ratio,gamma) # Estimated exit mach number for calculated are ratio

    F = pd.read_csv(r'C:/CaseyRocket/Data/Force.csv') # Load Cell Force Data     #add tkinter just open file system and select data
    F = F.iloc[:,0].values  # iloc: = integer location based indexing
                            # iloc[:,0] means : select all rows, 0 selects the first column 
                            # .values converts panda series into np array

    Pc = pd.read_csv(r'C:/CaseyRocket/Data/Pressure.csv') # Pressure Transducer (Dynamic Pressure aka chamber Pressure)
    Pc = Pc.iloc[:,0].values  

    num_samples, sampling_freq, dt, t = DataInformation(F) # See DataInformation()
    
    F = LowPassFilter(F, sampling_freq) # force values filtered by low pass filter
    max_F = max(F) * 4.448 # lbf to Newtons

    calculated_burn_time, burn_force = CalcStartStopBurn(F, t, sampling_freq, Aerotech_Thrust_Duration) # returns burn time in seconds and an array with burn force only
    calculated_mass_flow_rate = CalcultateMassFlowRate(Aerotech_Mass, calculated_burn_time, Aerotech_Mass_Fow_Rate) # returns calculated mass flow rate based on excel data
    calculated_Ve = CalculateExitVelocity(burn_force, calculated_mass_flow_rate, Aerotech_Ve)


if __name__ == "__main__":
    main()
