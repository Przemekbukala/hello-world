"""
Core computational module for the fuel consumption estimator.
"""
import random
from numba import njit
import pint

si = pint.UnitRegistry()

@njit
def _simulate_trip_engine(distance_km: int, base_fuel_per_km: float) -> float:
    """
    Simulates fuel consumption on a kilometer-by-kilometer.
    Parameters:
        distance_km (int): The total trip distance in kilometers.
        base_fuel_per_km (float): The base fuel consumption in liters per 1 km.
        
    Returns:
        float: The total estimated fuel consumption in liters.
    """
    total_fuel = 0.0
    for _ in range(distance_km):
        random_factor = 0.8 + random.random() * 0.7 
        total_fuel += base_fuel_per_km * random_factor
    return total_fuel

def estimate_trip_fuel(distance, base_consumption_per_100km):
    """
    Estimate the total fuel consumption for a given trip.
    Parameters:
        distance: Trip distance.
        base_consumption_per_100km: Average fuel consumption with units (liters per 100 km).
    Returns:
        The total estimated volume of fuel.
    """
    if not distance.check('[length]'):
        raise pint.DimensionalityError(distance.units, 'meter')
    dist_km = int(distance.m_as('kilometer'))
    liters_per_km = base_consumption_per_100km.m_as('liter / kilometer')
    total_liters = _simulate_trip_engine(dist_km, liters_per_km)
    return total_liters * si.liter