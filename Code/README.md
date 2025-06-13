
# 📊 PlotData – Burn Data Visualization and Filtering

This section documents how to use the `PlotData` scripts for loading, processing, and visualizing hot fire test data from a solid rocket motor.

---

## Overview

The `PlotData.py` script is used to:
- Import raw sensor data from `.csv` files
- Show raw voltage readings from both the load cell and pressure transducer
- Apply a low-pass Butterworth filter to remove noise
- Display filtered vs. unfiltered thrust and chamber pressure data




---

## 📁 File Structure and Function Descriptions

- **functions.py**: Contains reusable functions for filtering, plotting, and analyzing the data.
- **PlotData.py**: Imports `functions.py` and uses it to load `.csv` files and display results in grid plots.

---

## 📂 Input Files Required

To use this script, you’ll need the following files placed in a folder:
- `Force.csv`: Filtered load cell data (converted to lbf)
- `Pressure.csv`: Filtered chamber pressure (psi)
- `RawLoadCell.csv`: Raw voltage from load cell
- `RawPressureTransducer.csv`: Raw voltage from pressure transducer

---

## How to Use

1. Make sure all dependencies are installed:
```bash
pip install numpy pandas matplotlib scipy
```

2. Replace the placeholder file paths (e.g. `C:/CaseyRocket/Data/Force.csv`) in `PlotData.py` with the actual path to the CSV files on your machine. For example:
```python
pd.read_csv(r'C:/YourPath/Force.csv')
```
3. Make sure both `PlotData.py` and `functions.py` are in the same directory.

4. Run `PlotData.py`. It will:
   - Import and process the CSV data
   - Apply a filter to the data
   - Plot 4 figures: raw and filtered comparisons for force and chamber pressure

---

##  Additional Info

- Data is assumed to be sampled at **2000 Hz** for **15 seconds**, totaling **30,000 samples**.
- Filtering is done using a **4th-order low-pass Butterworth filter** with a **cutoff of 7 Hz but can be changed directly**.


---


