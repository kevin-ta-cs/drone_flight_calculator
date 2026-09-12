import pytest
from flight_calculator import calculate_flight_time


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        calculate_flight_time(-1)


def test_calculate_flight_time_zero_weight_returns_full_flight_time():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_regular_weight_uses_formula():
    assert calculate_flight_time(250) == pytest.approx(155.0)


def test_calculate_flight_time_exact_zero_boundary():
    assert calculate_flight_time(1800) == pytest.approx(0.0)


def test_calculate_flight_time_clamps_to_zero_for_large_weights():
    assert calculate_flight_time(2000) == pytest.approx(0.0)