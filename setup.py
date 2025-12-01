"""Setup configuration for Mauritanian Elections package."""
from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="mauritanian-elections",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Exploratory data analysis of Mauritanian presidential elections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mauritanianelections",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "bokeh>=2.4.0",
        "geopandas>=0.10.0",
        "jupyter>=1.0.0",
        "folium>=0.12.0",
    ],
    entry_points={
        "console_scripts": [
            "analyze-2019=mauritanian_elections.analysis.election_2019:run_2019_analysis",
            "analyze-2024=mauritanian_elections.analysis.election_2024:run_2024_analysis",
            "analyze-poverty=mauritanian_elections.analysis.poverty:run_poverty_analysis",
        ],
    },
)
