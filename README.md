# PR.10_Final_Project
# COVID-19 Data Analysis and Visualization

A Python-based data analytics project that processes, analyzes, and visualizes historical COVID-19 data trends across multiple countries using **Pandas**, **Matplotlib**, and **Seaborn**.

## Project Overview
This project fulfills the foundational guidelines for the Skill Education curriculum. It uses structural tracking matrices to evaluate the spread of COVID-19 over time by examining total confirmed cases, new cases, and total mortality data across different regions.

## Features
- **Data Loading & Preprocessing:** Cleans and processes structured records dynamically using Pandas DataFrames.
- **Trend Analysis:** Tracks cumulative distribution metrics and growth parameters over chronological intervals.
- **Data Visualizations:** 
  - *Line Plot:* Total confirmed cases over time to identify growth trajectories.
  - *Scatter Plot:* Relationship evaluation between total registered cases and total reported deaths.
  - *Bar Plot:* Comparative analysis of daily new registered cases across target countries.

## Repository & Project Structure
```text
├── covid_data.csv        # Organized comma-separated values data matrix
├── covid_analysis.py    # Main pipeline automation script
└── README.md             # Project documentation guide
```

## Prerequisites & Installation
Ensure you have Python 3.x installed on your workstation. Install the required data science libraries using the pipeline installation manager:

```bash
pip install pandas matplotlib seaborn
```

## Dataset Configuration (`covid_data.csv`)
The project reads data locally from a structured matrix file named `covid_data.csv`. The schema contains the following data elements:
- `location`: Name of the target country.
- `date`: Timestamp recording interval (YYYY-MM-DD).
- `total_cases`: Cumulative count of confirmed cases.
- `total_deaths`: Cumulative count of recorded deaths.
- `new_cases`: Active daily registered metrics.

## Execution Guide
1. Place both `covid_data.csv` and `covid_analysis.py` in the exact same directory.
2. Open your terminal or command prompt interface.
3. Execute the core process controller:

```bash
python covid_analysis.py
```

## Output Visualizations
Upon successful execution, the script will automatically render and save the following high-definition chart images to your active directory:
- `total_cases_trend.png`
- `cases_vs_deaths.png`
- `new_cases_comparison.png`
