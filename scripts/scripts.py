import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error

def extent_per_year(df):
    """
    Bar chart of Arctic SIE measurements per year
    :param df: obj, pandas dataframe 
    :return barplot: plot,  
    """

    # Create year and month columns
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month

    # Count values per year
    df = df.groupby('year')['extent_million_sq_km'].count().reset_index(name='measurements_taken')

    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    # Plot number of measurements taken per year
    plot_ = sns.barplot(df, x="year", y="measurements_taken")
    plt.title('Arctic Sea Ice Extent: Measurements Per Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Count')

    for ind, label in enumerate(plot_.get_xticklabels()):
        if ind % 5 == 0:  # every 5th label is kept
            label.set_visible(True)
        else:
            label.set_visible(False)

    plt.savefig('figures/measurements_per_year.png')
    plt.show()

    print("Measurements were taken approximately every 2 days from 1978 to 1987.") 
    print("From 1988 to 2023, there is a daily measurement recorded, showing the recording frequency was increased two-fold.")

def seasonality(df):
    """
    Create time series plot to observe seasonality.
    :param df: obj, cleaned sea ice dataframe
    :return lineplot: plot,
    """

    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    # Plot time series of SIE
    sns.lineplot(x="date", y="extent_million_sq_km", data=df)

    max_year = pd.DatetimeIndex(df['date']).year.max()

    plt.title(f"Arctic Sea Ice Extent: 1978-{max_year}")
    plt.xlabel("Year")
    plt.ylabel("Extent (M km^2)")

    # Save and plot figure
    plt.savefig(f'figures/ts_1978_{max_year}.png')
    plt.show()

    print("The above set is non-stationary as there are clear annual changes in sea ice extent.")

# def get_date_ranges(start_date, mid_date, end_date):
#     """
#     Count the number of months between dates.
#     :param start_date: date
#     :param end_date: date
#     """
#     # Set range parameters 
#     start_date = start_date  # start of time series
#     mid_date = mid_date  # Sep 11, 2001
#     end_date = end_date  # end of time series

#     # Count number of months before 9-11-2021 & count number of months prior
#     date_range_before = pd.date_range(start=start_date, end=mid_date, freq='MS')
#     event_minus_n = len(date_range_before)

#     # Count number of months after 9-11-2021 & count number of months after
#     date_range_after = pd.date_range(start=mid_date, end=end_date, freq='MS')
#     event_plus_n = len(date_range_after)

#     print(f"n-months prior to 9/11: {event_minus_n}")
#     print(f"n-months after 9/11: {event_plus_n}")
#     print(f"% of real versus forecasted: {round((event_plus_n / event_minus_n), 2) * 100}%")


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