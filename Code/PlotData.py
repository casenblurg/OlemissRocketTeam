import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 


def main():
    Force = pd.read_csv(r'C:/CaseyRocket/Data/Force.csv')     # Read Force Data from Excel
    F = Force.iloc[:,0].values 

    ChamberPressure = pd.read_csv(r'C:/CaseyRocket/Data/Pressure.csv') # Read Pressure Data from Excel
    Pc = ChamberPressure.iloc[:,0].values 

    RawLoadCell = pd.read_csv(r'C:/CaseyRocket/Data/RawLoadCell.csv')     # Read Force Data from Excel
    RawF = RawLoadCell.iloc[:,0].values 

    RawPressureTransducer = pd.read_csv(r'C:/CaseyRocket/Data/RawPressureTransducer.csv') # Read Pressure Data from Excel
    RawP = RawPressureTransducer.iloc[:,0].values 

    func.DataInformation(F)  # PlotBurnData() Depends on this function call !
    func.PlotBurnData(F, Pc, RawF, RawP, 0)  

    Filtered_F = func.LowPassFilter(F)
    Filtered_Pc = func.LowPassFilter(Pc)

    func.PlotBurnData(Filtered_F, Filtered_Pc, F, Pc, 1) # if filtered aka 1, then RawF becomes F and F becomes Filtered F, then Rawp becomes P and P becomes Filtered P


if __name__ == "__main__":
    main()
