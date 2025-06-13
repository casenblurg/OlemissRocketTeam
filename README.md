# Overview

Over the course of a year and a half (Nov 2023 - April 2025) I instrumented a solid rocket motor (SRM) test stand. This data acquisition system (DAQ)  was developed to accurately record thrust and chamber pressure data from Aerotech solid rocket motors during static fire tests. The system captures static thrust and pressure data from both a load cell and a pressure transducer, conditions the signals, and stores the data for post-processing and analysis.

## Hardware
| Component                              | Description                                              |
|----------------------------------------|----------------------------------------------------------|
| **NI cDAQ-9174**                       | Chassis for data acquisition modules                    |
| **NI 9201**                            | 12-bit Analog Input Module (used to read sensor voltages) |
| **NI 9482**                            | Electromechanical Relay Module                          |
| **DR-ODC5**                            | Solid-state relay (used for ignition)                   |
| **PS-1S400EP**                         | Power Supply Unit                                       |
| **Computer Supply Breakout Board**     | Provides regulated voltage                              |
| **INA110**                             | Instrumentation Amplifier (for load cell signal conditioning) |
| **LC113B-2K Omega S-type Load Cell**   | Measures thrust (lbf)                                   |
| **PX309-3KG10V Omega Pressure Transducer** | Measures chamber pressure (psi)                     |
| **1 µF Tantalum Capacitors**           | Used for filtering power supply noise                   |
| **General wiring, connectors, and test stand** | Electrical and mechanical support components       |
