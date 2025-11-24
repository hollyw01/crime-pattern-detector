# Crime Pattern Detector

A data analysis project exploring patterns and hotspots in UK street-level crime data.

This project fetches open data from the UK Police API, stores it locally, and cleans it
into a structured format ready for visualisation and further analysis. It is part of
my MSc Computer Science portfolio.

---

## 🔍 Project goals

- Download real-world crime data from an open API
- Clean and structure the raw JSON data
- Prepare the data for visualisation and modelling (e.g. trends, hotspots)
- Demonstrate practical skills in Python, data handling, and reproducible workflows

---

## 🗂️ Repository structure

```text
crime-pattern-detector/
├── data/
│   ├── raw/          # Raw JSON downloaded from the API
│   └── processed/    # Cleaned CSV files ready for analysis
├── notebooks/        # Jupyter notebooks for exploration (to be added)
├── src/
│   ├── fetch_data.py # Download crime data from the UK Police API
│   └── clean_data.py # Clean raw JSON into a tabular CSV
├── requirements.txt  # Python dependencies
├── LICENSE
└── README.md
