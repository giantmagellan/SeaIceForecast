import pandas as pd
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

def metric_report(pred_set):
    """
    :param pred_set: df, prediction set
    :return results: df, results report
    """

    # Outcome Variable parameter
    outcome_var = pred_set['extent_million_sq_km']

    # Calculate Evaluation Metrics
    rmse_fc, mape_fc = eval_metrics(outcome_var, pred_set['naive_forecast'])
    rmse_sa, mape_sa = eval_metrics(outcome_var, pred_set['simple_avg_forecast'])
    rmse_ma, mape_ma = eval_metrics(outcome_var, pred_set['moving_avg_forecast'])
    rmse_hw, mape_hw = eval_metrics(outcome_var, pred_set['holt_winter_forecast'])
    rmse_sarima, mape_sarima = eval_metrics(outcome_var, pred_set['sarima'])

    # Print Evaluation Results
    results = pd.DataFrame({'Method':['Naive Forecast', 
                                    'Simple Average', 
                                    'Moving Average',
                                    'Holt-Winters',
                                    'SARIMA'
                                    ], 
                            'MAPE': [mape_fc, mape_sa, mape_ma, mape_hw, mape_sarima], 
                            'RMSE': [rmse_fc, rmse_sa, rmse_ma, rmse_hw, rmse_sarima],
                            'Forecast': [pred_set['naive_forecast'].iloc[0], 
                                        pred_set['simple_avg_forecast'].iloc[0],
                                        pred_set['moving_avg_forecast'].iloc[0],
                                        None,
                                        None]})
    print(results)
