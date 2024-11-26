# Immo-Eliza-project
Data analysis

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Timeline](#timeline)
- [Project status](#project-status)
  
## Description
This is the second stage of a larger project to create a Machine Learning (ML) model to predict sell prices of real estate properties in Belgium. The current task is to clean and preprocess the collected data in the previous stage. 

The Python-based tool uses `cleaned_dataset_analysis (1).csv` file in the first analysis, and then in further analysis is used `no_outliers_dataset.csv`

**The csv file has the following:**
- 10875 rows and 22 columns

- 12 categorical variables: Locality, Zip Code, Province,Type of Property, Subtype of Property, PEB, State of the Building, 
Fully Equipped Kitchen, Furnished, Open Fire, Terrace, Garden, Swimming Pool, Subtype of Property_Grouped

- 8 numeric variables: Price, Number of Rooms, Livable Space (m2), Terrace Area (m2), Garden Area (m2), 
Surface of the Land (m2), Number of Facades, Primary Energy Consumption (kWh/m2)


## Installation
1. Clone the repository: ``` git clone https://github.com/BeatrizJover/Data_analysis``
2. Install dependencies: 
  - ```Python 3.12.4```  
  - ```pip install pandas seaborn matplotlib plotly jupyter```
3. Version:
Pandas 2.2.2
Matplotlib 3.9.2
Seaborn 0.13.2
jupyternotebook: 7.2.2

## Usage
- In data_analysis folder you will find notebooks with the graphs and analysis of the real estate market.
- On the olha-branch you can find two files 'first_data_modifications.ipynb' and 'charts.ipynb' with code, as well as a folder 'charts' with visualizations.

## Contributors
The project was made by a group of Junior AI & Data Scientists (in alphabetical order):

- [BeatrizJover](https://github.com/BeatrizJover)
- [Miro](https://github.com/MiroFronhoffs)
- [Olha](https://github.com/olhasl)

## Timeline
- This stage of the project lasted 4 days in the week of 22/11/2024 12:30.

## Project status
- [Build status](https://trello.com/b/y2RZys6x/data-analysis)
