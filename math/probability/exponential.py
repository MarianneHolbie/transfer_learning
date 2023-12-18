#!/usr/bin/env python3
"""
    Class to represent an exponential distribution
"""


class Exponential:
    """
        Class to represent an exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
            Class constructor

            :param data : List of the data to estimate the distribution
            :param lambtha : Expected number of occurrences

        """

        if data is None:
            # Use the given lambtha
            self.lambtha = float(lambtha)
            # check lambtha is positive
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            # calculate lambtha from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # lambtha is the inverse of the mean of the data
            self.lambtha = 1 / (sum(data) / len(data))
