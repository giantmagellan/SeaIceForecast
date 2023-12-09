import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

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

def convert_date_formats(df, col):
    """
    Convert dates to YYYY-MM-DD format.
    :param df: obj, pandas dataframe 
    :param col: str, column name
    :return df: obj, 
    """
    # Check for date, time, or datetime columns
    # date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    # print(date_cols)
    # TODO: Apply standard date format YYYY-MM-DD
    # TODO: Create new columns for date, time, and seasons
    
    # Example date
    # event_date = 'Sep-01'

    # for col in date_cols:
        # Convert to datetime format
    df[col] = pd.to_datetime(df[col], format='%b-%y')

    # df.loc[df[col].dt.strftime('%b-%y') == event_date, col] = \
    #     df[df[col].dt.strftime('%b-%y') == event_date][col].dt.strftime('%Y-%m')

    # Find start and end date formats
    # print(f"Start date row: {df[df[col] == '2001-09-01']}")
    # print(f"End date row:{df.tail(1)}")
    return df

def order_by_date(df):
    """ 
    Order the dataframe by datetime in ascending order.
    :param df: obj, return ed
    """
    # Order time series
    df = df.sort_values(by=col)

    return df 

def get_date_ranges(start_date, mid_date, end_date):
    """
    Count the number of months between dates.
    :param start_date: date
    :param end_date: date
    """
    # Set range parameters 
    start_date = start_date  # start of time series
    mid_date = mid_date  # Sep 11, 2001
    end_date = end_date  # end of time series

    # Count number of months before 9-11-2021 & count number of months prior
    date_range_before = pd.date_range(start=start_date, end=mid_date, freq='MS')
    event_minus_n = len(date_range_before)

    # Count number of months after 9-11-2021 & count number of months after
    date_range_after = pd.date_range(start=mid_date, end=end_date, freq='MS')
    event_plus_n = len(date_range_after)

    print(f"n-months prior to 9/11: {event_minus_n}")
    print(f"n-months after 9/11: {event_plus_n}")
    print(f"% of real versus forecasted: {round((event_plus_n / event_minus_n), 2) * 100}%")


def standard_formatter(df):
    """
    Convert ingestion data into a standard format.
    :param df: obj, pandas dataframe
    :return df: obj, updated dataframe
    """
    # Format column names
    df = convert_column_names(df)

    # Format datetime columns and create seasons
    df = convert_date_formats(df)

    return df


"""Tasks to automate"""
# Count missing values per column
# TODO: Apply impute method
# na_counts = df.isna().sum().to_dict()
# print(pd.DataFrame(na_counts, index=[0]))

# TODO: Report summary statisitcs
# TODO: Eliminate duplicate dates

def calculate_rmse(outcome_var, forecast):
    """
    Calculate RMSE.
    :param outcome_var: series, variable to be forecasted.
    :param forecast: series, forecasted series.
    :return rmse: float, root mean squared error
    """
    return np.sqrt(mean_squared_error(outcome_var, forecast)).round(2)

def calculate_mape(outcome_var, forecast):
    """
    Calculate MAPE.
    :param outcome_var: series, variable to be forecasted.
    :param forecast: series, forecasted series.
    :return mape: float, mean absolute percentage error
    """
    return np.round(np.mean(np.abs(outcome_var - forecast) / outcome_var) * 100, 2)

# TODO: iterate over all forecasted metrics and output as single dataframe
def eval_metrics(test_set, forecast_set):

    rmse = calculate_rmse(test_set, forecast_set)
    mape = calculate_mape(test_set, forecast_set)

    return rmse, mape