"""Configuration and path management for Mauritanian Elections analysis."""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
SHAPE_DIR = DATA_DIR / "shape"

# Output directories
OUTPUT_DIR = BASE_DIR / "output"
FIGURES_DIR = OUTPUT_DIR / "figures"
HTML_DIR = OUTPUT_DIR / "html"

# Data files
ELECTION_2019_CSV = DATA_DIR / "RIMResultatElection2019.csv"
ELECTION_2024_CSV = DATA_DIR / "RIMResultatElection2024.csv"
POVERTY_CSV = DATA_DIR / "dataset.csv"

# Shapefiles
SHAPEFILE_ADM1 = SHAPE_DIR / "mrt_admbnda_adm1_gov_20200801.shp"
SHAPEFILE_ADM2 = SHAPE_DIR / "mrt_admbnda_adm2_gov_20200801.shp"

# Ensure output directories exist
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)
