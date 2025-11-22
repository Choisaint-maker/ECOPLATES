# ECOPLATES — Automated Paper Recycling Machine  
### Python + Raspberry Pi Pico + Electro-Pneumatic System

Ecoplates is an automated machine designed to transform waste paper into new recycled sheets through a fully controlled electro-pneumatic process.  
This project was developed as my high-school graduation work and later expanded as a personal initiative in industrial automation, sustainability, and embedded systems.

The system integrates **Python-based control**, **Raspberry Pi Pico microcontroller**, **pneumatic actuators**, and a full **industrial-like workflow** that includes pulp preparation, molding, pressing, and drying.

---

## 🔍 Overview  

![SolidWorks Render](media/RenderSolidworks.png)

Ecoplates demostrates a complete production pipeline (with the material ready; mixing paper and water in equal parts):

1. Pulp preparation  
2. Mold filling  
3. Automated pressing  
4. Drying and final sheet extraction  

By combining embedded control with air-driven actuators, the machine produces recycled paper with minimal manual intervention.

This project was built using affordable components and aims to be replicable for schools, community workshops, and sustainability programs.

---

## 🧠 System Architecture  
The machine uses a **Raspberry Pi Pico** running **MicroPython** to execute a sequential control loop.  
The architecture includes:

- Raspberry Pi Pico (central controller)  
- Python/MicroPython automation scripts  
- Solenoid valves  
- Pneumatic cylinders  
- Limit switches and sensors  
- Power system for actuators  
- Custom mechanical structure made from recycled and machined components
  ![Full Mechanical Schematic](media/FullSchematic.png)

A block diagram of the system reflects:

- Input stage (paper + water)  
- Mechanical processing (pulp generation)  
- Molding and pressing  
- Output stage (recycled sheet)

---

## ⚙️ Hardware & Electronics  
- **Microcontroller:** Raspberry Pi Pico  
- **Programming language:** Python (MicroPython)  
- **Actuation:** Electro-pneumatic valves + linear cylinders  
- **Sensors:** End-stops / position sensors  
- **Power:** Independent pneumatic and electronic supply  
- **Structure:** Steel, aluminum and 3D-printed components
   ![Electric/Control and Strengh Schematic](media/Strengh-Logical-Circuits.png)
  ![Pneumatic Schematic](media/Electropneumatic%20schematic.png)

---

## 💻 Software  
The control software includes:

- Step-based sequence automation  
- Timing control for actuators  
- Safety interlock logic  
- Modular Python scripts  
- Configurable execution parameters  

All code is included in the `/code` folder.

---

## 📸 Media (Photos & Videos)  
Real images and recordings of the machine in operation are available in:

- `/photos`
- `/videos`

These documents show:
- the assembly process  
- the electro-pneumatic system  
- the recycled sheets produced  
- testing phases  
- the machine operating autonomously  

---

## 📄 Documentation  
Full academic documentation of the project:

- **Monografía Ecoplates (project thesis)** – in `/docs`  
- **Carpeta de Desarrollo (development notebook)** – in `/docs`  

These include theoretical background, process flow definition, calculations, diagrams, and evaluation results.

---

## 🎯 Results  
The machine successfully produced recycled sheets using automated control.  
The tests confirmed:

- stable pneumatic operation  
- reliable control loop in Python  
- adequate pressing force  
- repeatable sheet formation  
- safe sequence execution  

The project validated the feasibility of low-cost automated recycling systems.

---

## 🚀 Future Improvements  
Planned enhancements:

- moisture sensor for drying automation  
- graphical interface for process monitoring  
- redesigned pressing module  
- full enclosure for operator safety  
- improved mold system  
- fully portable version  

---

## 👤 Authors  
**Santiago Gonzalez (Choisaint)** — Mechatronics Engineering Student 
Personal portfolio: https://github.com/choisaint
**Johan Hurtado** — Software Engineering Student
**David Acosta** — Electrical Engineering Student


---
