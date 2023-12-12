import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import statsmodels.tsa.api as smt
import statsmodels.api as sm
import pmdarima as pm

def forecast(train_set, test_set):
    """
    Create forecasts for Naive, Simple Avg, and Moving Avg forecasts.
    :param train_set: df, training dataframe
    :param test_set: df, testing dataframe
    :return y_hat: df, copy of test set with forecasted values
    """

    # Forecast types and labels
    fc_types = ['naive_forecast', 'simple_avg_forecast', 'moving_avg_forecast', 'holt_winter_forecast']
    labels = ['Naive', 'Simple Average', 'Moving Average', 'Holt-Winters']

    # Copy test set
    y_hat = test_set.copy()
    train_len = len(train_set)

    # Set plot parameters
    plt.figure(figsize=(10, 4))
    plt.grid(color='grey', linestyle='-', linewidth=0.25)

    # Iterate over each forecasting method
    for type, label in zip(fc_types, labels):
        # Create forecast parameter
        if type == fc_types[0]:
            y_hat[type] = train_set['extent_million_sq_km'][train_len-1]
        if type == fc_types[1]:
            # Average previously observed points
            y_hat[type] = train_set['extent_million_sq_km'].mean()
        if type == fc_types[2]:
            # Create moving average forecast for each cycle (365 days)
            y_hat[type] = train_set['extent_million_sq_km'].rolling(365).mean().iloc[-1]
        if type == fc_types[3]:
            # Fit Holt-Winters algorithm w/ 4 seasonal periods of 365 days each
            fit_hw = smt.ExponentialSmoothing(np.asarray(train_set['extent_million_sq_km']), 
                                  seasonal_periods=365*4, trend='add', seasonal='add',).fit()
            y_hat['holt_winter_forecast'] = fit_hw.forecast(len(test_set))

        # Plot Train and Test sets
        plt.plot(train_set['extent_million_sq_km'], label='Train')
        plt.plot(test_set['extent_million_sq_km'], label='Test')
        plt.plot(y_hat[type], label=label)
        
        plt.legend(loc='best')
        plt.title(f'Arctic Sea Ice Extent: {label} Forecast')
        plt.xlabel('Index')
        plt.ylabel('Extent (M km^2)')

        plt.savefig(f'figures/sie_{type}.png')
        plt.show()

    return y_hat

def sarima(train_set, test_set, predictions):
    """
    Create SARIMA forecast
    :param train_set: df, training dataframe
    :param test_set: df, testing dataframe
    :param predictions: df, prediction set
    :return predictions: df, copy of test set with forecasted values (y_hat)
    """

    # Fit your model
    model = pm.auto_arima(train_set['extent_million_sq_km'], seasonal=True, m=12)

    # Create forecasts by predicting N steps into the future
    predictions['sarima'] = model.predict(test_set['extent_million_sq_km'].shape[0])

    # Visualize SARIMA forecasts
    plt.figure(figsize=(10,4))
    plt.grid(color='grey', linestyle='-', linewidth=0.25)

    plt.plot(train_set['extent_million_sq_km'], label='Train')
    plt.plot(test_set['extent_million_sq_km'], label='Test')
    plt.plot(predictions['sarima'], label='SARIMA Forecast')

    plt.title('Arctic Sea Ice Extent: SARIMA Forecast')
    plt.xlabel('Index')
    plt.ylabel('Extent (M km^2)')
    plt.legend(loc='best')
    plt.show()

    return predictions