"""Analysis module for poverty correlation with election data."""
import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.mauritanian_elections import config
from src.mauritanian_elections.data_loader import load_election_data, load_shapefile
from src.mauritanian_elections.visualization import create_poverty_map


def run_poverty_analysis():
    """Run poverty correlation analysis."""
    print("Loading poverty data...")
    poverty = load_election_data(config.POVERTY_CSV, sep=";")
    print(f"Loaded {len(poverty)} rows")
    
    print("\nLoading shapefile...")
    gdf = load_shapefile(config.SHAPEFILE_ADM1)
    print(f"Loaded {len(gdf)} regions")
    
    print("\nProcessing poverty data...")
    # Extract relevant columns
    wilaya = poverty[["willaya", "p0", "p1_", "p2_"]].copy()
    
    # Calculate poverty index
    wilaya["wilaya_index"] = wilaya[["p0", "p1_", "p2_"]].mean(axis=1)
    
    # Group by wilaya
    wilaya = wilaya.groupby("willaya", as_index=False).mean()
    
    # Create wilaya mapping
    wilayas_map = {
        "Hodh ech Chargui": "MR07",
        "Hodh el Gharbi": "MR08",
        "Assaba": "MR02",
        "Gorgol": "MR05",
        "Brakna": "MR03",
        "Trarza": "MR12",
        "Adrar": "MR01",
        "Dakhlet Nouadhibou": "MR04",
        "Tagant": "MR11",
        "Guidimaka": "MR06",
        "Tiris Zemmour": "MR13",
        "Inchiri": "MR09",
        "Nouakchott": "MR10"
    }
    
    wilaya['ADM1_PCODE'] = wilaya.willaya.map(wilayas_map)
    
    print("\nMerging with geodata...")
    newpoverty = gdf.merge(wilaya, on='ADM1_PCODE')
    print(f"Merged data has {len(newpoverty)} rows")
    
    print("\nGenerating poverty map...")
    map_path = config.FIGURES_DIR / "poverty_map.png"
    create_poverty_map(newpoverty, column='wilaya_index', 
                      title="Poverty Index by Wilaya",
                      output_path=str(map_path))
    
    print(f"\n✓ Poverty analysis complete!")
    print(f"  - Map saved to: {map_path}")
    
    return newpoverty


if __name__ == "__main__":
    run_poverty_analysis()
