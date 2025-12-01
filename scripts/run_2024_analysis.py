#!/usr/bin/env python3
"""Run 2024 election analysis."""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.mauritanian_elections.analysis.election_2024 import run_2024_analysis

if __name__ == "__main__":
    run_2024_analysis()
