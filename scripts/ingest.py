from urllib.request import urlretrieve
from pathlib import Path
import pandas as pd
import datetime

def retrieve_sie_data():
     """ 
     Retrieve Arctic Sea Ice Data.
     Source: Sea Ice Index NSIDC data set G02135 """
     # Url containing sea ice data download
     url = (
          "https://noaadata.apps.nsidc.org/NOAA/G02135/seaice_analysis/Sea_Ice_Index_Daily_Extent_G02135_v3.0.xlsx"
     )

     # Download date
     today = datetime.datetime.now().strftime('%Y%m%d')
     
     filename = f"../data/staging/arctic_sie_g02135_{today}.xlsx"
     path = Path(__file__).parent / filename

     # Retrieve dataset
     urlretrieve(url, path)

     print(f'Staging path: {filename}')

     return path

def convert_column_names(df):
    """
    Convert column names to lower case and replace spaces with underscores.
    :param df: obj, pandas dataframe
    :return df: obj, updated dataframe w/ reformatted column names
    """
    # Convert to lower case and replaces spaces
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    # Remove underscores from column name endings
    validate_cols = [col for col in df.columns if col.endswith('_')]
    for col in validate_cols:
        new_col_name = col[:-1]
        df.rename(columns={col: new_col_name}, inplace=True)

    print(f"Reformatted column names: {df.columns}")
    return df

def sie_index_transformer():
    """
    Transform Sea Ice Index Data into standardized format.
    :return df: transformed dataframe
    """

    # Retrieve then import excel sheet download from NSIDC
    filename = retrieve_sie_data()
    
    df = pd.read_excel(filename, sheet_name='NH-Daily-Extent', index_col=[0])

    # Drop unneccessary columns
    df = df.drop(columns=['1981-2010 mean', '1981-2010 median', ' '])

    # Merge month and day hierarchical index
    df.index = df.index + '-' + df['Unnamed: 1'].astype(str)

    # Drop remaining day number column, then transpose and reset dataframe index
    df = df.drop(columns=['Unnamed: 1']).transpose().reset_index()

    # Use the melt method to transform dates and measurements into individual columns
    df = pd.melt(df, id_vars=['index'], var_name='day', value_name='extent_million_sq_km')

    # Merge index (year) column with month and day columns
    df['index'] = df['index'].astype(str)
    df['date'] = df['index'] + '-' + df['day']

    # Drop unneccessary index (year) and day columns
    df = df.drop(['index', 'day'], axis=1).dropna()
    
    # Convert date to pandas datetime format YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date'])

    # Validate column names
    df = convert_column_names(df)

    # Sort and reset index
    df = df.sort_values('date', ascending=True).reset_index(drop=True)

    # Save to training directory
    today = datetime.datetime.now().strftime('%Y%m%d')
    filename = f'../data/training/arctic_sie_clean_{today}.csv'

    print(f'Training path: {filename}')
    
    dest_path = Path(__file__).parent / filename
    df.to_csv(dest_path)

    return df

