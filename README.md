# Crime Pattern Detector

A data analysis project exploring patterns and hotspots in UK street-level crime data.  
This project fetches open data from the UK Police API, stores it locally, and cleans it into a structured format ready for visualisation and further analysis. It is part of my MSc Computer Science portfolio.

---

## 🔍 Project Goals

- Download real-world crime data from an open API  
- Clean and structure the raw JSON data  
- Explore crime trends using Python and Jupyter  
- Demonstrate practical skills in data handling, visualisation, and reproducible workflows  

---

## 🗂 Repository Structure

```text
crime-pattern-detector/
├── data/
│   ├── raw/          # Raw JSON downloaded from the API
│   └── processed/    # Cleaned CSV files ready for analysis
├── notebooks/        # Jupyter notebooks for exploration
├── src/
│   ├── fetch_data.py # Download crime data from the UK Police API
│   └── clean_data.py # Convert raw JSON to a clean CSV dataset
├── requirements.txt  # Python dependencies
├── LICENSE
└── README.md
