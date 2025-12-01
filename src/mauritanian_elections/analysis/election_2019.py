"""Analysis module for 2019 Mauritanian presidential election."""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.mauritanian_elections import config
from src.mauritanian_elections.data_loader import (
    load_election_data,
    load_shapefile,
    preprocess_2019_data,
    group_by_candidate_wilaya
)
from src.mauritanian_elections.visualization import (
    create_candidate_bar_chart,
    create_pie_chart,
    create_static_bar_chart,
    create_static_pie_chart,
    save_bokeh_plot
)


def run_2019_analysis():
    """Run complete analysis for 2019 election data."""
    print("Loading 2019 election data...")
    data = load_election_data(config.ELECTION_2019_CSV, sep=";")
    print(f"Loaded {len(data)} rows")
    
    print("\nLoading shapefile...")
    gdf = load_shapefile(config.SHAPEFILE_ADM2)
    print(f"Loaded {len(gdf)} regions")
    
    print("\nPreprocessing data...")
    election = preprocess_2019_data(data)
    
    print("\nGrouping by candidate and wilaya...")
    grouped_cand = group_by_candidate_wilaya(election)
    print(f"Grouped into {len(grouped_cand)} rows")
    
    print("\nGenerating visualizations...")
    
    # Create bar chart
    bar_chart_path = config.HTML_DIR / "2019_votes_by_wilaya.html"
    print(f"Creating bar chart: {bar_chart_path}")
    create_candidate_bar_chart(grouped_cand, str(bar_chart_path))
    
    # Create static bar chart
    static_bar_path = config.FIGURES_DIR / "2019_votes_by_wilaya.png"
    print(f"Creating static bar chart: {static_bar_path}")
    create_static_bar_chart(grouped_cand, title="2019 Votes by Candidate and Wilaya", 
                           output_path=str(static_bar_path))
    
    # Create pie chart
    pie_chart_path = config.HTML_DIR / "2019_vote_distribution.html"
    print(f"Creating pie chart: {pie_chart_path}")
    create_pie_chart(grouped_cand, output_path=str(pie_chart_path))
    
    # Create static pie chart
    static_pie_path = config.FIGURES_DIR / "2019_vote_distribution.png"
    print(f"Creating static pie chart: {static_pie_path}")
    create_static_pie_chart(grouped_cand, title="2019 Vote Distribution", 
                           output_path=str(static_pie_path))
    
    print("\n✓ 2019 analysis complete!")
    print(f"  - Bar chart saved to: {bar_chart_path}")
    print(f"  - Static bar chart saved to: {static_bar_path}")
    print(f"  - Pie chart saved to: {pie_chart_path}")
    print(f"  - Static pie chart saved to: {static_pie_path}")
    
    return grouped_cand


if __name__ == "__main__":
    run_2019_analysis()
