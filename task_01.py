#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some conversions."""

ABSOLUTE_DIFFERENCE = 273.15


def fahrenhiet_to_celsius(degrees):

    """This function converts the temperature in Fahrenhiet to celsius.

    Args:
        degrees (mixed): temperature measurement
        fc (decimal): value

    returns:
        temperature in celcius

    Example:
        >>>fahrenhiet_to_celsius(30.0)
        -1.111
    """
    fc = fahrenhiet_to_celsius(degrees) = (degrees - 32) * 5) / 9
    return fc


def celsius_to_kelvin(degrees):

    """This function converts the temperature in celsius to kelvin.

    Args:
        degrees (mixed): temperature value
        ck (decimal): value

    returns:
        temperature in kelvin

    Example:
        >>>celsius_to_kelvin(10)
        283.15
    """
    
    ck = degrees + ABSOLUTE_DIFFERENCE
    return ck


def fahrenhiet_to_kelvin(degrees):
    """This function converts the temperature in fahrenheit to kelvin.

    Args:
       degrees (mixes): temperature measurement
       fk (decimal): values

    returns:
       temperature in kelvin

    Examples:
        >>> fahrenhiet_to_kelvin(30.2)
        272.26
    """
    
    fc = fahrenhiet_to_celsius(degrees)
    fk = celsius_to_kelvin(fc)
    return fk
    fk = fc + ABSOLUTE_DIFFERENCE
    return fk
