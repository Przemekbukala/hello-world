"""
Monte Carlo Fuel Consumption Estimator Package.
This package provides tools to estimate vehicle fuel consumption using Monte Carlo 
simulations.
"""
from .core import estimate_trip_fuel, si
__all__ = ["estimate_trip_fuel", "si"]