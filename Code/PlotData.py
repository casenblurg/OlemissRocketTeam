import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 


def main():
    
    F, Pc, RawF, RawP = func.GetBurnData()
    
    
    func.DataInformation(F, 15)  # PlotBurnData() Depends on this function call !
    func.PlotBurnData(F, Pc, RawF, RawP, 0)  

    Filtered_F = func.LowPassFilter(F)
    Filtered_Pc = func.LowPassFilter(Pc)

    func.PlotBurnData(Filtered_F, Filtered_Pc, F, Pc, 1) # if filtered aka 1, then RawF becomes F and F becomes Filtered F, then Rawp becomes P and P becomes Filtered P


if __name__ == "__main__":
    main()
