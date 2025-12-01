"""Visualization utilities for Mauritanian Elections analysis."""
from bokeh.plotting import figure, show, output_file, save
from bokeh.colors import named
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20c
from bokeh.transform import cumsum, dodge
from bokeh.io import export_png
import bokeh.plotting as bp
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_static_bar_chart(grouped_data, title="Votes by Candidate and Wilaya", output_path=None):
    """
    Create a static bar chart using seaborn.
    
    Args:
        grouped_data: Grouped election data
        title: Chart title
        output_path: Optional path to save the figure
    """
    plt.figure(figsize=(15, 8))
    sns.set_theme(style="whitegrid")
    
    # Create bar plot
    chart = sns.barplot(
        data=grouped_data,
        x="Wilaya",
        y="nbVoix",
        hue="prenom",
        palette="tab10"
    )
    
    plt.title(title, fontsize=16)
    plt.xlabel("Wilaya", fontsize=12)
    plt.ylabel("Number of Votes", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Candidate", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    
    return chart


def create_static_pie_chart(data, candidate_col='prenom', votes_col='nbVoix', 
                          title="Vote Distribution", output_path=None):
    """
    Create a static pie chart using matplotlib.
    
    Args:
        data: Election data
        candidate_col: Column name for candidates
        votes_col: Column name for votes
        title: Chart title
        output_path: Optional path to save the figure
    """
    # Aggregate votes
    vote_totals = data.groupby(candidate_col)[votes_col].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 10))
    
    # Create pie chart
    plt.pie(vote_totals, labels=vote_totals.index, autopct='%1.1f%%',
            startangle=90, pctdistance=0.85)
    
    # Draw circle for donut chart
    centre_circle = plt.Circle((0,0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    plt.title(title, fontsize=16)
    plt.axis('equal')
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()


def create_candidate_bar_chart(grouped_data, output_path=None):
    """
    Create a bar chart showing votes by candidate and wilaya.
    
    Args:
        grouped_data: Grouped election data
        output_path: Optional path to save the HTML output
        
    Returns:
        bokeh.plotting.figure: The created figure
    """
    # Get unique candidates and wilayas
    candidates = grouped_data['prenom'].unique().tolist()
    wilayas = grouped_data['Wilaya'].unique().tolist()
    
    # Prepare data
    data = {'wilayas': wilayas}
    for candidate in candidates:
        candidate_data = grouped_data[grouped_data['prenom'] == candidate]
        votes = []
        for wilaya in wilayas:
            wilaya_votes = candidate_data[candidate_data['Wilaya'] == wilaya]['nbVoix'].values
            votes.append(wilaya_votes[0] if len(wilaya_votes) > 0 else 0)
        data[candidate] = votes
    
    source = ColumnDataSource(data=data)
    
    # Create figure
    p = figure(x_range=wilayas, height=600, width=1200,
               title="Votes by Candidate and Wilaya",
               toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset,save")
    
    # Add bars for each candidate
    colors = Category20c[len(candidates)] if len(candidates) <= 20 else Category20c[20]
    
    for i, candidate in enumerate(candidates):
        p.vbar(x=dodge('wilayas', -0.25 + i * 0.5 / len(candidates), range=p.x_range),
               top=candidate, width=0.5 / len(candidates), source=source,
               color=colors[i % len(colors)], legend_label=candidate)
    
    p.xgrid.grid_line_color = None
    p.legend.location = "top_right"
    p.legend.orientation = "vertical"
    p.xaxis.major_label_orientation = pi / 4
    
    if output_path:
        output_file(output_path)
        save(p)
    
    return p


def create_pie_chart(data, candidate_col='prenom', votes_col='nbVoix', 
                     title="Vote Distribution", output_path=None):
    """
    Create a pie chart showing vote distribution.
    
    Args:
        data: Election data
        candidate_col: Column name for candidates
        votes_col: Column name for votes
        title: Chart title
        output_path: Optional path to save the HTML output
        
    Returns:
        bokeh.plotting.figure: The created figure
    """
    # Aggregate votes by candidate
    vote_totals = data.groupby(candidate_col)[votes_col].sum().reset_index()
    vote_totals['angle'] = vote_totals[votes_col] / vote_totals[votes_col].sum() * 2 * pi
    vote_totals['color'] = Category20c[len(vote_totals)]
    
    p = figure(height=600, width=800, title=title,
               toolbar_location=None, tools="hover", 
               tooltips=f"@{candidate_col}: @{votes_col}",
               x_range=(-0.5, 1.0))
    
    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white", fill_color='color',
            legend_field=candidate_col, source=vote_totals)
    
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    
    if output_path:
        output_file(output_path)
        save(p)
    
    return p


def create_poverty_map(gdf, column='wilaya_index', title="Poverty Index by Wilaya",
                       output_path=None, figsize=(15, 15)):
    """
    Create a choropleth map showing poverty index.
    
    Args:
        gdf: GeoDataFrame with geometry and poverty data
        column: Column to visualize
        title: Map title
        output_path: Optional path to save the figure
        figsize: Figure size tuple
        
    Returns:
        matplotlib.figure.Figure: The created figure
    """
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    
    gdf.plot(column=column, 
             ax=ax,
             edgecolor="green",
             cmap=plt.cm.Blues,
             legend=True,
             legend_kwds={"label": "% Poverty in Mauritania"})
    
    ax.set_title(title, fontsize=16)
    ax.axis('off')
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    return fig


def save_bokeh_plot(plot, filepath):
    """
    Save a Bokeh plot to HTML file.
    
    Args:
        plot: Bokeh plot object
        filepath: Path to save the HTML file
    """
    output_file(filepath)
    save(plot)
