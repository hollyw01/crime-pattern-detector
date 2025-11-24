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

## 📁 Repository Structure

```text
crime-pattern-detector/
├── data/
│   ├── raw/          # Raw JSON downloaded from the API
│   └── processed/    # Cleaned CSV files ready for analysis
├── notebooks/        # Jupyter notebooks for exploration and advanced analysis
├── src/
│   ├── fetch_data.py # Download crime data from the UK Police API
│   └── clean_data.py # Convert raw JSON into a clean CSV dataset
├── requirements.txt  # Python dependencies
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.x**
- **requests** – API calls  
- **pandas** – data processing  
- **matplotlib** – visualisation  
- **seaborn** – heatmaps  
- **scikit-learn** – clustering  
- **Jupyter Notebook** – exploration & visualisation  

---

## ▶️ How to Run the Project Locally

Requires **Python 3**.

### 1) Clone the repository

```bash
git clone https://github.com/hollywg01/crime-pattern-detector.git
cd crime-pattern-detector
```

---

## 📥 Step 1 — Fetch Raw Crime Data

Run the following script to download raw crime data from the UK Police API:

```bash
python src/fetch_data.py
```

---

## 📓 Notebooks

Interactive Jupyter notebooks for data exploration and advanced analysis:

- [`crime_pattern_exploration.ipynb`](https://github.com/hollywg01/crime-pattern-detector/blob/main/notebooks/crime_pattern_exploration.ipynb)  
  *Exploratory analysis of crime categories, trends, summary statistics, and location visualisation.*

- [`crime_pattern_advanced.ipynb`](https://github.com/hollywg01/crime-pattern-detector/blob/main/notebooks/crime_pattern_advanced.ipynb)  
  *Heatmaps, top streets analysis, and spatial clustering using K-Means.*

---

## 💡 Future Improvements

- Add geographical hotspot mapping (Folium / Plotly)  
- Introduce time-series analysis or forecasting  
- Add command-line arguments to choose location/date  
- Build an interactive dashboard using Streamlit  

---

## 📫 Contact

Created by **Holly Williams-Gardner**  
- GitHub: https://github.com/hollywg01  
- LinkedIn: https://www.linkedin.com/in/holly-w-aab8721a0
