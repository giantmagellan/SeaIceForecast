import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

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