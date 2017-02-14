from __future__ import division
from utils import open_csv, parse_data, make_copy, average, prev_values

csv_path = '../indicatorservice/data/sma.csv'
raw_data = parse_data(open_csv(csv_path))


def upper_envelope(sma, envelope=0.025):
    return sma + sma * envelope


def lower_envelope(sma, envelope=0.025):
    return sma - sma * envelope


def simple_moving_average(data, period=20, envelope=2.5):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    percentage_envelope = envelope / 100
    # First data
    output = [average(prev_values(data, i, period))
              for i, v in enumerate(data)]
    return [(sma, upper_envelope(sma, percentage_envelope), lower_envelope(sma, percentage_envelope))
            for sma in output]

# Calculate the SMA
def test (data):
    # Make a copy
    data = make_copy(raw_data)

    # Filter the close prices
    close_prices = [d['close'] for d in data]
    sma = simple_moving_average(close_prices, 10)
    for i, v in enumerate(sma):
      print i + 1, v, '\n'

# test(raw_data)