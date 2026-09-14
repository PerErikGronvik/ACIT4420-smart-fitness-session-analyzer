"""
Validation functions
"""

def validate_observation(observation_dict: dict) -> tuple[bool, str]:
    """
    Validate an observation dictionary.

    Args:
        Observation data (dict)
    Returns:
       Tuple of is_valid (bool) and error_message (str).
    """
    required_keys = ["timestamp", "heart_rate", "skin_response", "temperature", "activity_level", "signal_quality"]
    for key in required_keys:
        if key not in observation_dict:
            return False, f"Missing required key: {key}"
    try:
        timestamp = observation_dict["timestamp"]
        heart_rate = observation_dict["heart_rate"]
        skin_response = observation_dict["skin_response"]
        temperature = observation_dict["temperature"]
        activity_level = observation_dict["activity_level"]
        signal_quality = observation_dict["signal_quality"]

        if not (30 <= heart_rate <= 230):
            return False, "Heart rate must be between 30 and 230."
        if not (0.0 <= skin_response <= 1.0):
            return False, "Skin response must be between 0.0 and 1.0."
        if not (30 <= temperature <= 42):
            return False, "Temperature must be between 30 and 42."
        if not (0.0 <= activity_level <= 1.0):
            return False, "Activity level must be between 0.0 and 1.0."
        if not (0.0 <= signal_quality <= 1.0):
            return False, "Signal quality must be between 0.0 and 1.0."

        return True, ""
    except Exception as e:
        return False, str(e)

def is_good_signal_quality(signal_quality: float, threshold: float = 0.5) -> bool:
    """
    Check if the signal quality in the observation is good.

    Args:
        Signal quality value (float)
    Returns:
        True if signal quality is good (>= threshold), False otherwise.
    """
    return 0.0 <= signal_quality <= 1.0 and signal_quality >= threshold