"""
Calculation functions
"""

def calculate_average(values: list[float]) -> float:
    """
    Calculate the average of a list of numeric values.

    Args:
        values: List of numeric values (float)
    Returns:
        The average of the values.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_min(values: list[float]) -> float:
    """
    Find the minimum value

    Args:
        values: Numeric values (float)
    Returns:
        The smallest value.
    """
    if not values:
        return 0.0
    return min(values)

def calculate_max(values: list[float]) -> float:
    """
    Find the maximum value

    Args:
        values: Numeric values (float)
    Returns:
        The highest value.
    """
    if not values:
        return 0.0
    return max(values)

def calculate_hr_elevation(current_hr_value: float, resting_hr_value: int) -> float:
    """
    Calculate the elevation in heart rate from the resting heart rate.

    Args:
        The current heart rate (float)
        The resting heart rate (int)
    Returns:
        The elevation in heart rate.
    """
    return current_hr_value - resting_hr_value

def detect_recovery(
    observations: list["Observation"],
    resting_hr_value: int,
    treshold: float = 0.2,
) -> bool:
    """
    Detect if the heart rate is recovering based on observations and threshold.

    Args:
        observations
        resting_hr_value (int)
        treshold: The threshold to check for recovery (float)
    Returns:
        True if recovery is detected, False otherwise.
    """
    if len(observations) < 8:
        return False

    last_8 = observations[-8:]
    last_4 = observations[-4:]

    last_8_hr = calculate_average([o.heart_rate for o in last_8])
    last_4_hr = calculate_average([o.heart_rate for o in last_4])
    last_8_distance = abs(last_8_hr - resting_hr_value)
    last_4_distance = abs(last_4_hr - resting_hr_value)
    heart_rate_recovering = (
        last_8_distance > 0
        and ((last_8_distance - last_4_distance) / last_8_distance) > treshold
    )

    last_8_activity = calculate_average([o.activity_level for o in last_8])
    last_4_activity = calculate_average([o.activity_level for o in last_4])
    activity_decreasing = last_8_activity > last_4_activity

    return heart_rate_recovering and activity_decreasing