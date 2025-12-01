# 🗳️ Mauritanian Elections - Exploratory Data Analysis

This repository contains exploratory data analysis (EDA) on the results of the **2019** and **2024 presidential elections in Mauritania**. It combines data visualization, geospatial mapping, and basic socio-economic correlation analysis to better understand voting patterns across different regions.

---

## 📁 Project Structure

```
mauritanianelections/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup file
├── .gitignore                   # Git ignore file
├── data/                        # Data files
│   ├── RIMResultatElection2019.csv
│   ├── RIMResultatElection2024.csv
│   ├── dataset.csv
│   └── shape/                   # Shapefiles for mapping
├── notebooks/                   # Jupyter notebooks
│   ├── 2019.ipynb              # 2019 election analysis
│   ├── 2024.ipynb              # 2024 election analysis
│   └── poverty.ipynb           # Poverty correlation analysis
├── src/                         # Source code
│   └── mauritanian_elections/  # Main package
│       ├── config.py           # Configuration and paths
│       ├── data_loader.py      # Data loading utilities
│       ├── visualization.py    # Visualization functions
│       └── analysis/           # Analysis modules
│           ├── election_2019.py
│           ├── election_2024.py
│           └── poverty.py
├── scripts/                     # Executable scripts
│   ├── run_2019_analysis.py
│   ├── run_2024_analysis.py
│   └── run_poverty_analysis.py
└── output/                      # Generated outputs
    ├── figures/                 # PNG/JPG figures
    └── html/                    # Interactive HTML plots
```

---

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
   ```bash
   cd /Users/abdu07/Desktop/PROJECTS/mauritanianelections
   ```

2. **Activate virtual environment** (already created):
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install package in development mode** (optional):
   ```bash
   pip install -e .
   ```

---

## 📊 Usage

### Running Analysis Scripts

You can run the analysis scripts directly:

```bash
# Activate virtual environment first
source venv/bin/activate

# Run 2019 election analysis
python scripts/run_2019_analysis.py

# Run 2024 election analysis
python scripts/run_2024_analysis.py

# Run poverty correlation analysis
python scripts/run_poverty_analysis.py
```

### Using Jupyter Notebooks

The original Jupyter notebooks are preserved in the `notebooks/` directory:

```bash
# Activate virtual environment
source venv/bin/activate

# Start Jupyter
jupyter notebook

# Navigate to notebooks/ and open desired notebook
```

### Programmatic Usage

You can also import and use the modules in your own Python code:

```python
from src.mauritanian_elections.data_loader import load_election_data, preprocess_2019_data
from src.mauritanian_elections.visualization import create_pie_chart

# Load and preprocess data
data = load_election_data("data/RIMResultatElection2019.csv", sep=";")
election = preprocess_2019_data(data)

# Create visualization
create_pie_chart(election, output_path="output/html/my_chart.html")
```

---

## 📊 Key Analyses

- 📌 **Turnout analysis** by region and candidate
- 📌 **Comparison between 2019 and 2024** vote trends
- 📌 **Poverty vs voting behavior** exploration
- 📌 **Interactive visualizations** using [Bokeh](https://bokeh.org)
- 📌 **Geospatial mapping** with shapefiles for regional insights

---

## 🗺️ Outputs

The analysis scripts generate:

- **HTML files**: Interactive Bokeh visualizations in `output/html/`
- **PNG/JPG files**: Static maps and charts in `output/figures/`

Example outputs:
- `output/html/2019_votes_by_wilaya.html` - Bar chart of votes by region
- `output/html/2024_vote_distribution.html` - Pie chart of vote distribution
- `output/figures/poverty_map.png` - Choropleth map of poverty index

---

## 🔧 Dependencies

This project uses:

- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `matplotlib` / `seaborn` - Static visualizations
- `bokeh` - Interactive visualizations
- `geopandas` - Geospatial data handling
- `jupyter` - Notebook interface
- `folium` - Interactive maps

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 📌 About

This is an independent data science project focused on Mauritania's democratic data. It is meant for educational and analytical purposes only.

---

## 📝 License

This project is open source and available for educational purposes.
