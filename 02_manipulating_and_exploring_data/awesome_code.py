"""
This script contains an awesome function that
fixes longitude values.
"""

def awesome_longitude_fix(lon_array):
    """
    Fixes longitude values to be between 0 & 360

    Parameters
    ----------
    lon_array : array-like
        array of longitude values that needs to be fixed

    Return
    ------
    lon_array : array-like
        longitude array between 0 & 360
    """
    condition_less = lon_array < 0
    condition_greater = lon_array >= 360
    lon_array[condition_less] += 180
    lon_array[condition_greater] -= 180
    return lon_array
