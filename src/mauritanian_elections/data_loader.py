"""Data loading utilities for Mauritanian Elections analysis."""
import pandas as pd
import geopandas
import warnings

warnings.filterwarnings("ignore")


def load_election_data(filepath, sep=";"):
    """
    Load election data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        sep: Separator character (default: ";")
        
    Returns:
        pandas.DataFrame: Loaded election data
    """
    return pd.read_csv(filepath, sep=sep)


def load_shapefile(filepath):
    """
    Load shapefile data using geopandas.
    
    Args:
        filepath: Path to the shapefile
        
    Returns:
        geopandas.GeoDataFrame: Loaded shapefile data
    """
    return geopandas.read_file(filepath)


def preprocess_2019_data(data):
    """
    Preprocess 2019 election data.
    
    Args:
        data: Raw election data DataFrame
        
    Returns:
        pandas.DataFrame: Preprocessed data
    """
    # Extract relevant columns
    election = data[['Wilaya', 'nbSuffrage', 'nbVoix', 'Moughataa', 'Candidat', 'CodeWilaya']].copy()
    
    # Extract last name as prenom
    election['prenom'] = election['Candidat'].apply(lambda x: x.split()[-1])
    
    # Define replacements for candidate names
    replacements = {
        'Abdi': 'Hamadi',
        'M\'Bareck': 'El Id',
        'Abeid': 'Biram'
    }
    
    # Replace the modalities in the 'prenom' column
    election['prenom'] = election['prenom'].replace(replacements)
    
    # Normalize Moughataa names
    election['Moughataa'] = (election['Moughataa']
                             .str.normalize('NFKD')
                             .str.encode('ascii', errors='ignore')
                             .str.decode('utf-8')
                             .str.lower())
    
    return election


def preprocess_2024_data(data):
    """
    Preprocess 2024 election data.
    
    Args:
        data: Raw election data DataFrame
        
    Returns:
        pandas.DataFrame: Preprocessed data
    """
    # Calculate nbSuffrage
    data['nbSuffrage'] = data['nb_bulletin'] - data['nb_votant_null'] - data['nb_votant_neutre']
    
    # Select and rename columns to match 2019 format
    selected_columns = [
        'codeWilaya', 'Wilaya', 'MoughataaFr', 'Commune', 'Center', 'bureau',
        'nbr_Inscrits', 'nb_bulletin', 'nb_votant_null', 'nb_votant_neutre', 
        'nb_vote', 'Candidat', 'nbSuffrage'
    ]
    
    data = data[selected_columns].copy()
    
    # Rename columns
    data.columns = [
        'CodeWilaya', 'Wilaya', 'Moughataa', 'Commune', 'Center', 'CodeBureau',
        'NbInscrits', 'nbVotant', 'nbVoteNull', 'nbVoteNeutre', 'nbVoix', 
        'Candidat', 'nbSuffrage'
    ]
    
    # Extract relevant columns for analysis
    election = data[['Wilaya', 'nbSuffrage', 'nbVoix', 'Moughataa', 'Candidat', 'CodeWilaya']].copy()
    
    # Extract last name
    election['prenom'] = election['Candidat'].apply(lambda x: x.split()[-1])
    
    # Replacements for 2024
    replacements = {
        'Abdi': 'Hamadi',
        'M\'Bareck': 'El Id',
        'Abeid': 'Biram'
    }
    
    election['prenom'] = election['prenom'].replace(replacements)
    
    # Normalize Moughataa
    election['Moughataa'] = (election['Moughataa']
                             .str.normalize('NFKD')
                             .str.encode('ascii', errors='ignore')
                             .str.decode('utf-8')
                             .str.lower())
    
    return election


def group_by_candidate_wilaya(election_data):
    """
    Group election data by candidate and wilaya.
    
    Args:
        election_data: Preprocessed election DataFrame
        
    Returns:
        pandas.DataFrame: Grouped data
    """
    grouped = election_data.groupby(['prenom', 'Wilaya'], as_index=False).agg({
        'nbSuffrage': 'sum',
        'nbVoix': 'sum',
        'Moughataa': 'first',
        'Candidat': 'first',
        'CodeWilaya': 'first'
    })
    
    return grouped
