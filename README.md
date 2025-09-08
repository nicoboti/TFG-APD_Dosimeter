# TFG-APD_Dosimeter
This repository contains all the resources related to my Bachelor’s Thesis project, focused on the design and implementation of a compact radiation dosimeter using a **Silicon Avalanche Photodiode (APD)**, analog front-end circuitry, and a **ESP32-C3 microcontroller** for digital readout and wireless communication.

## 📂 Repository Structure

- **`kicad_files/`**  
  Contains the **circuit design and PCB layout files** created with KiCad.  
  This includes schematics, board layouts, and related project files.  

- **`ltspice_sims/`**  
  Includes **LTspice simulation files (`.asc`)** used to verify the proper functioning of the circuit before building it physically.  
  ⚠️ Note: raw output data files (`.txt`) from simulations are not included here due to their large size.  

- **`python_scripts/`**  
  Contains **Python scripts** related to the ESP32-C3 microcontroller and additional data analysis:  
  - Firmware code (MicroPython) for signal acquisition and Wi-Fi communication.  
  - Python code for plotting and analyzing simulation results.  

- **`docs/`**  
  Miscellaneous **documents related to the project**, such as draft reports, additional notes, and supporting files.  

- **`photos/`**  
  Contains **pictures of the physical project**, including the circuit assembly, soldering process, oscilloscope captures, and other relevant images.  

---

## 🛠️ Tools Used

- **KiCad** – Circuit and PCB design.  
- **LTspice** – Analog circuit simulations.  
- **Python / MicroPython** – Firmware development and data analysis.  

---

## 📸 Project Overview

This project implements a compact dosimeter system, structured in the following stages:  
1. **Detection:** A Silicon Avalanche Photodiode (APD) detects ionizing radiation.  
2. **Analog front-end:** The APD signal is conditioned using a transimpedance amplifier (OPA657) and further stages.  
3. **Digitalization:** The conditioned signal is read by the **ADC of the ESP32-C3**, programmed in MicroPython.  
4. **Wireless communication:** Data is transmitted in real time via **Wi-Fi**.  
5. **Analysis:** Simulation and experimental data are analyzed using Python scripts.  

---

⚡ *This repository serves as the complete source of designs, simulations, firmware, and documentation developed during the project.*
