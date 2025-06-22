import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 


def main():
    
    F, Pc, RawF, RawP = func.GetBurnData()
    
    total_t = 15

    func.DataInformation(F, total_t)  # PlotBurnData() Depends on this function call !
    func.PlotBurnData(F, Pc, RawF, RawP, 0)  

    cutoff = 7
    order = 4

    Filtered_F = func.LowPassFilter(F, cutoff, order)
    Filtered_Pc = func.LowPassFilter(Pc, cutoff, order)

    func.PlotBurnData(Filtered_F, Filtered_Pc, F, Pc, 1) # if filtered aka 1, then RawF becomes F and F becomes Filtered F, then Rawp becomes P and P becomes Filtered P


if __name__ == "__main__":
    main()
