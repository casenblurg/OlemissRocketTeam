# 📊 Data Collection Overview

This folder contains raw and processed data collected during solid rocket motor (SRM) static fire tests. The data acquisition system was configured to sample both **chamber pressure** and **thrust** at a **rate of 2,000 Hz**, resulting in **30,000 data points** over a **15-second** burn duration.

---

##  Sampling Rate Information

###  Collection
- **Sampling Rate (fs):** 2,000 Hz  
- **Test Duration (t):** 15 seconds  
- **Total Data Points:**  
  fs × t = 2000 × 15 = **30,000 samples**

---

###  Pressure Transducer (PX309-3KGV)

- **Sample Rate:** 2,000 Hz  
- **Response Time:** ≈ 1 ms (per datasheet)  
- **Estimated Bandwidth:**  
  B ≈ 0.35 / Response Time  
  → B ≈ 0.35 / 0.001 s = **350 Hz**

- **Nyquist Criterion:**  
  fs > 2 × B  
  → 2000 Hz > 700 Hz ✅

---

###  Load Cell (LC113B-2K)

- **Sample Rate:** 2,000 Hz  
- **Estimated Response Time:** 2–5 ms (typical for S-type load cells)  
- **Estimated Bandwidth:**  
  B ≈ 0.35 / 0.002 s = **175 Hz**

- **Nyquist Criterion:**  
  fs > 2 × B  
  → 2000 Hz > 350 Hz ✅

---

## ✅ Summary

The 2,000 Hz sampling rate satisfies the Nyquist Theorem for both sensors and ensures accurate time-domain capture of fast transients in thrust and chamber pressure data. A total of **30,000 samples** per channel were collected over the 15-second window, providing high-resolution insight into motor behavior.
