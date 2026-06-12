# Multi-Criteria Screening of Salt Hydrates for Thermochemical Energy Storage

This project was developed to compare and rank several salt hydrates that may be suitable for thermochemical energy storage applications. The evaluation is based on three criteria: energy density, stability, and cost.

The material data are provided in a CSV file. The script reads the data, normalizes each criterion, and calculates an overall score using predefined weighting factors. The materials are then ranked according to their final scores.

The weighting factors used in this study are:

* Energy Density: 50%
* Stability: 30%
* Cost: 20%

After the analysis is completed, the program automatically creates a results folder and saves:

* A ranked list of materials (ranked_materials.csv)
* An energy density comparison plot (Figure1_EnergyDensity.png)
* A final score comparison plot (Figure2_FinalScore.png)

To run the program, place the input file (data.csv) in the project directory and execute:

python screening.py

Required Python packages:

* pandas
* matplotlib

This work was conducted as a preliminary material screening study to identify promising salt hydrates for further investigation in thermal energy storage systems.

# Author:

**Md Hasibul Hasan**

B.Sc. in Mechanical Engineering

Rajshahi University of Engineering & Technology

# References:
* https://www.energy.gov/sites/default/files/2023-06/bto-peer-2023-36424-deve-ndsu-gladen.pdf
* https://www.energy.gov/cmei/buildings/articles/development-novel-thermochemical-nanocellulose-based-material-thermal