# 🚀 SRM Static Fire Data Analysis

This repository contains Python code for analyzing the static fire test data of a solid rocket motor (SRM) — specifically the **AeroTech L1420R-PS RMS-75/5120** motor used by the **Ole Miss Rocket Team**. The script processes force and pressure sensor data to extract useful performance parameters such as:

- Burn time
- Mass flow rate
- Exit velocity
- Area ratio
- Exit Mach number
- Comparison against AeroTech's published data

---

## 📁 Files

- `SRM_Calculations.py` — Main Python script for processing and analyzing test data
- `Force.csv` — Load cell data (in lbf)
- `Pressure.csv` — Chamber pressure data (not yet utilized)
- `README.md` — Project description and usage instructions

---

## 📊 Output Metrics

| Parameter               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Burn Time**          | Based on when thrust rises above and falls below zero                      |
| **Mass Flow Rate**     | Computed using motor mass and burn duration                                 |
| **Exit Velocity (Ve)** | `Ve = F_avg / mdot`                                                          |
| **Exit Mach Number**   | Estimated using area ratio and isentropic relations                         |
| **Specific Impulse**   | `Isp = Ve / g0`, shows thrust per unit propellant per second                |

> 💡 For theoretical background, refer to:
> - [NASA: Isentropic Flow Calculator](https://www.grc.nasa.gov/www/k-12/airplane/astar.html)
> - [Purdue: Isentropic Flow Table Generator](https://engineering.purdue.edu/~propulsi/propulsion/flow/isent12.html)
> - [NASA: Specific Impulse Explanation](https://www.grc.nasa.gov/www/k-12/airplane/specimp.html)

---

## 📐 AeroTech Reference Data

| Property               | Value                    |
|------------------------|--------------------------|
| Average Thrust         | 1420 N                   |
| Total Impulse          | 4603 Ns                  |
| Burn Duration          | 3.2 s                    |
| Motor Mass             | 2560 g                   |
| Throat Diameter        | 0.485 in                 |
| Exit Diameter          | 1.250 in                 |

📄 Official Motor Spec Sheets:
- [AeroTech Product Page](https://aerotech-rocketry.com/products/product_3872d294-577c-353f-9773-6594597dfda3?_pos=2&_sid=036e31a62&_ss=r)
- [Throat/Nozzle Dimensions Reference](https://www.rocketmotorparts.com/75mm_Nozzle_0485__Throat/p1577809_20627885.aspx)

---




   ## 📦 Dependencies

Make sure to install the correct Python dependencies:

```bash
pip install numpy pandas matplotlib scipy
