




# 🗳️ Mauritanian Elections - Exploratory Data Analysis

This repository contains exploratory data analysis (EDA) on the results of the **2019** and **2024 presidential elections in Mauritania**. It combines data visualization, geospatial mapping, and basic socio-economic correlation analysis to better understand voting patterns across different regions.

---

## 📁 Project Structure

```

election/
├── 2019.ipynb                   # EDA for 2019 election data
├── 2024.ipynb                   # EDA for 2024 election data
├── poverty.ipynb               # Exploration of poverty-vote correlation
├── dataset.csv                 # Merged dataset (if applicable)
├── RIMResultatElection2019.csv # Raw 2019 election results
├── RIMResultatElection2024.csv # Raw 2024 election results
├── shape/                      # Geospatial shapefiles (Wilaya boundaries)
├── bokehviz.py                 # Interactive visualization with Bokeh
├── wilaya\_vote.html/.jpg       # Regional vote map exports
└── Bokeh Plot.html/.jpg        # Interactive dashboard export

````

---

## 📊 Key Analyses

- 📌 **Turnout analysis** by region and candidate
- 📌 **Comparison between 2019 and 2024** vote trends
- 📌 **Poverty vs voting behavior** exploration
- 📌 **Interactive visualizations** using [Bokeh](https://bokeh.org)
- 📌 **Geospatial mapping** with shapefiles for regional insights

---

## 🗺️ Visuals

The project includes dynamic HTML-based maps and plots showing:
- Votes per candidate per region
- Turnout heatmaps
- Regional socio-economic overlays

---

## 🔧 Dependencies

This project uses:

- `pandas`
- `matplotlib` / `seaborn`
- `bokeh`
- `geopandas`
- `jupyter`

Install with:
```bash
pip install -r requirements.txt
````

---

## 📌 About

This is an independent data science project focused on Mauritania's democratic data. It is meant for educational and analytical purposes only.





