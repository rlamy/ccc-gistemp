"""
Numpy-based utilities for step5.
"""

import numpy as np
import scikits.timeseries as ts

from code import giss_data
from tool import giss_io

def from_subbox(subbox, start_date='1880-01', end_date='2010-12'):
    if subbox.good_count == 0:  #no data, contains only garbage
        series = ts.time_series([], freq='M')
    else:
        start = ts.Date('M', year=subbox.first_year, month=1)
        series = ts.time_series(np.ma.masked_values(subbox.series, 9999.),
                                freq='M', start_date=start)
    series = ts.adjust_endpoints(series, start_date=start_date, end_date=end_date)
    series.station_dist = getattr(subbox, 'd', np.nan)
    return series

def land_data():
    land = giss_io.SubboxReader(open('result/SBBX1880.Ts.GHCN.CL.PA.1200', 'rb'))
    land_it = iter(land)
    lmeta = next(land_it)
    return [from_subbox(sub) for sub in land_it]

def ocean_data():
    ocean = giss_io.SubboxReader(open('result/SBBX.HadR2', 'rb'))
    ocean_it = iter(ocean)
    ometa = next(ocean_it)
    return [from_subbox(sub) for sub in ocean_it]
