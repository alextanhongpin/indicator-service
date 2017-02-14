from __future__ import division
from utils import open_csv, parse_data, make_copy, average, prev_values
from simple_moving_average import simple_moving_average

csv_path = '../indicatorservice/data/sma.csv'
raw_data = parse_data(open_csv(csv_path))

def exponential_moving_average(data, period=20):
    """
      Calculates the EMA for a given time period
    """
    sma = simple_moving_average(data)[period]
    multiplier = ema_multiplier(period)
    return [var * (1 + multiplier) for val in sma]

def exponential_moving_average_multiplier(period):
    """
      Calculates the multiplier for the EMA
      based on the time period
    """
    return 2 / (period + 1)
