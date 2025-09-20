"""
Tests for the main application.
"""
import pytest
from main import calculate_sum


def test_calculate_sum():
    """Test the calculate_sum function."""
    # Test with positive numbers
    assert calculate_sum([1, 2, 3, 4, 5]) == 15
    
    # Test with empty list
    assert calculate_sum([]) == 0
    
    # Test with negative numbers
    assert calculate_sum([-1, -2, -3]) == -6
    
    # Test with mixed numbers
    assert calculate_sum([-1, 0, 1]) == 0


def test_calculate_sum_single_element():
    """Test calculate_sum with a single element."""
    assert calculate_sum([42]) == 42


def test_calculate_sum_floats():
    """Test calculate_sum with floating point numbers."""
    result = calculate_sum([1.5, 2.5, 3.0])
    assert abs(result - 7.0) < 0.001  # Using abs for float comparison
