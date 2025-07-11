import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as func 
import os
import LoadCellCalibration as Lcal


# time array 15 seconds total of burn data at 2 kHz
time = np.linspace(0,15,29999)
time_to_index = 30000 / 15


# Aerotech thrust data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "..", "Documents", "AeroTech_L1420R_ThrustData.csv"))

df = pd.read_csv(data_file, skiprows=3)

AerotechTime = df['Time (s)'].values
AerotechThrust = 0.225 * df['Thrust (N)'].values

AerotechTime = np.insert(AerotechTime, 0, 0)       # Insert 0 at index 0
AerotechThrust = np.insert(AerotechThrust, 0, 0)   # Insert 0 at index 0


#collect load cell data in volts
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2", "RawLoadCell_Test2.csv"))
F_voltage = pd.read_csv(data_file)     # Read Force Data from Excel
F_voltage = F_voltage.iloc[:,0].values 

# volts to lbf
m,b = Lcal.LoadCellCalibration()
Force_raw = (F_voltage * m) + b


# filter force data via lowpass 
order = 4
cutoff = 5
Force_filtered = func.LowPassFilter(Force_raw, cutoff, order)





# collect pressure data in volts
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.normpath(os.path.join(script_dir, "..", "BurnData","Test Burn 2", "Pressure_Test2.csv"))
Pressure = pd.read_csv(data_file)     # Read Force Data from Excel
Pressure = Pressure.iloc[:,0].values 





# volts to PSI






# filter pressure data via lowpass
order = 4
cutoff = 10
Pressure = func.LowPassFilter(Pressure, cutoff, order)


#get start and end burn : cut data
start = int(5.369*time_to_index)
end = int(8.697*time_to_index)

Force_filtered = Force_filtered[start:end]
Force_raw = Force_raw[start:end]

time = time[start:end]
time = time - time[0]


# plot raw force vs filtered force 
#plt.plot(AerotechTime, AerotechThrust, label=f"Aerotech Thrust Data (Burn Time: 3.2 s)", color='red')
#plt.plot(time,Force_filtered, label=f"Collected Thrust Data (Burn Time: {time[6655]:.2g} s)", color='blue')
#plt.title("Thrust vs Time: Aerotech Data vs Experimental Data")
#plt.xlabel("Time (s)")
#plt.ylabel("Thrust (lbs)")
#plt.legend()
#plt.grid()
#plt.show()




from matplotlib.lines import Line2D

# Compute max values and percent error
aero_max = np.max(AerotechThrust)
exp_max = np.max(Force_filtered)
percent_error = abs((exp_max - aero_max) / aero_max) * 100

# Set up figure with black background
plt.figure(facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')
ax.set_axisbelow(True)

# Make axis lines (spines) visible
for spine in ax.spines.values():
    spine.set_color('white')

# Define colors
aerotech_color = '#1f77b4'   # blue
filtered_color = '#df3a24'  # red-orange
text_color = 'white'

# Plot Aerotech data
plt.plot(AerotechTime, AerotechThrust,
         color=aerotech_color, linewidth=2, zorder=3)
plt.fill_between(AerotechTime, AerotechThrust, alpha=0.3, color=aerotech_color, zorder=1)

# Plot Experimental data
plt.plot(time, Force_filtered,
         color=filtered_color, linewidth=2, zorder=3)
plt.fill_between(time, Force_filtered, alpha=0.3, color=filtered_color, zorder=1)

# Create custom legend entries
aero_line = Line2D([], [], color=aerotech_color, linewidth=2)
exp_line = Line2D([], [], color=filtered_color, linewidth=2)
empty_line = Line2D([], [], color='black', linewidth=0)

plt.legend(
    handles=[aero_line, exp_line, empty_line],
    labels=[
        f"              Aerotech Thrust Data\n(Burn Time: 3.2 s) (Max Thrust: {aero_max:.1f} lbs)\n",
        f"            Experimental Thrust Data\n(Burn Time: {time[6655]:.1f} s) (Max Thrust: {exp_max:.1f} lbs)\n",
        f"       Max Thrust Percent Error: {percent_error:.2f}%",
    ],
    fontsize=15,
    handlelength=2,
    handletextpad=1.2,
    borderpad=1.2,
    facecolor='black',
    edgecolor='white',
    labelcolor='white'
)

# Grid and limits
plt.grid(color='gray', linestyle='--', linewidth=0.5, zorder=2)
plt.ylim(0, 450)

# Labels and formatting
plt.title("Thrust vs Time: Aerotech vs Experimental", fontsize=20, color=text_color)
plt.xlabel("Time (s)", fontsize=16, color=text_color)
plt.ylabel("Thrust (lbs)", fontsize=16, color=text_color)
plt.tick_params(labelsize=14, colors=text_color)

plt.tight_layout()
plt.show()