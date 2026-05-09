import pytest
import pint
from fuel_estimator.core import estimate_trip_fuel, si

def test_fuel_estimation_bounds():
    dist = 1000 * si.kilometer
    consumption = 8.0 * (si.liter / (100 * si.kilometer))
    result = estimate_trip_fuel(dist, consumption)
    min_expected = 10 * 8.0 * 0.8
    max_expected = 10 * 8.0 * 1.5
    assert result.check('[volume]')
    assert min_expected <= result.magnitude <= max_expected

def test_wrong_distance_unit():
    bad_dist = 100 * si.kilogram
    consumption = 8.0 * (si.liter / (100 * si.kilometer))
    with pytest.raises(pint.DimensionalityError):
        estimate_trip_fuel(bad_dist, consumption)
