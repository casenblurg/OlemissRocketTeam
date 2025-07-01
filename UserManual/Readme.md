
# SRM Test Stand User Manual 


## Contents

- Overview [x] 


- Hardware 
	- Omega [x]
		- Omega Load Cell (LC113B) [x]
		- Omega Pressure Transducer (PX309) [x]
	- National Instruments
		- DAQ (NI 9174) [x]
		- Analog Input Module (NI 9201) [x]
		- Electromechanical Relay (NI 9482)
	- Aerotech
		- Combustion Chamber
		- Reload Kit / Propellant


- Circuitry
	- Components
	- Design


- Software
	- NI LabView
	- Python
	- Excel
	- SolidWorks


- Sensor Calibration
	- Load Cell
	- Pressure Transducer


- SRM Testing
	- Safety
	- Test Burns
		- Pre-Test 
		- Test Day 
		- Post Test 

---
# Overview

The **SRM** (solid rocket motor) **test stand** was fabricated to aid in the testing and data collection of solid rocket motors during static burns. The test stand is capable of collecting combustion **chamber pressure** and rocket motor **thrust**. The project was **funded by the University of Mississippi** for the **Olemiss Rocket Team**. 

---
# Hardware

## Omega

There are two **Omega** sensors on the stand:

1. Omega Load Cell (LC113B)
2. Omega Pressure Transducer (PX309)

---
### Load Cell (LC113B)

[How do load cells work?](https://www.futek.com/how-a-load-cell-works?srsltid=AfmBOoodpjuVTFlQnRJYCVh5oO8KQaShKoqdbEF299_-5rnqHvmavmP9):

The load cell **converts an applied force into an output voltage** that we can measure. In this case the **[LCB113B-2K](https://www.dwyeromega.com/en-us/high-accuracy-stainless-steel-s-beam-load-cells/LC103B/p/LC113B-2K)** S-type load cell is used. This load cell is capable of withstanding **2000 lbs** of tension or compression. 

### Omega S-type load cell:

<img src="https://github.com/casenblurg/OlemissRocketTeam/blob/main/UserManual/Figures/LoadCell.png?raw=true" width="400">


---
## Pressure Transducer (PX309)
[How do pressure transducers work?](https://www.youtube.com/watch?v=UZLiLRlJzbU)

The pressure transducer **converts an applied pressure into an output voltage** that we can measure. In this case the **[PX309-3Kg10V](https://assets.omega.com/pdf/test-and-measurement-equipment/pressure/pressure-transducers/PX309.pdf)** pressure transducer is used. Again, this product contains a data sheet that provides all necessary information on the sensor.

### Omega Pressure Transducer:

<img src="https://github.com/casenblurg/OlemissRocketTeam/blob/main/UserManual/Figures/PressureTransducer.png?raw=true" width="400">


---

**How do we know what voltage corresponds to what force?:**


Every sensor has what is called a **[data sheet](https://assets.dwyeromega.com/spec/LC103B_spec.pdf)**, this is a **technical document provided by the manufacturer** that describes everything you need to know about a sensor — how it works, how to wire it, its limits, and how to interpret its output. Additionally, every sensor has an output sensitivity. **Output sensitivity** tells you **how much signal** a sensor gives **per supplied voltage**, usually in **millivolts per volt (mV/V)**. This will be further explained in the **sensor calibration** section.

---

# National Instruments

There are three **National Instruments** hardware components on the test stand:
1. NI cDAQ-9174
2. NI 9201 
3. NI 9482

---

## NI cDAQ-9174:

<img src="https://github.com/casenblurg/OlemissRocketTeam/blob/main/UserManual/Figures/cDaq.png?raw=true" width="400">

The NI cDAQ-9174 stands for **National Instruments Compact DAQ**. You can plug this into your computer using **USB** and run your Labview code. You can do all sorts of things depending on what module / card you have. In this case we have an analog input card and a relay card inserted into the cDAQ. 

## Analog Input Module (NI 9201):
<img src="https://github.com/casenblurg/OlemissRocketTeam/blob/main/UserManual/Figures/NI9201.png?raw=true" width="400">

This is a module that you plug in to the cDAQ, I like to think of it as a fancy multi meter. There are two main terminals to pay attention to, **COM** and **AI (analog in)**. If you were using this card as a multimeter, **COM** would go to your reference (**GND**) and **AI** would go to the voltage source you aretrying to read.

## Electromechanical Relay (NI 9482):

<img src="https://github.com/casenblurg/OlemissRocketTeam/blob/main/UserManual/Figures/ERELAY.png?raw=true" width="400">

This is another module that goes into the cDAQ. It is essentially a switch that can be programmed to turn on or off using Labview. This switch is used to ignite the rocket motor during test burns.

--- 

# Aerotech 
