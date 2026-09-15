"""
Grouping observations into fitness session.
"""

from src.observation import Observation
from src.validation import validate_observation, is_good_signal_quality
from src.calculations import calculate_average, calculate_min, calculate_max, calculate_hr_elevation

class Session:
    """
    Represents a fitness session consisting of multiple observations.
    
    Demonstrates composition: A session contains multiple observation objects.

    Attributes:
        observations (list of Observations in the p): The list of observations in the session.
        participant (Participant): The participant associated with the session.

    """
    def __init__(self, participant):

        self.observations = []
        self.participant = participant

    def add_observation(self, observation_dict: dict) -> tuple[bool, str]:
        """
        Adds an observation to the session after validation.

        Args:
            observation_dict (dict): The observation data to be added.

        Returns:
            tuple[bool, str]: A tuple containing a boolean indicating success,
                               and a message describing the result.
        """
        is_valid, message = validate_observation(observation_dict)
        if not is_valid:
            return False, message
        obs = Observation(
            timestamp=observation_dict["timestamp"],
            heart_rate=observation_dict["heart_rate"],
            skin_response=observation_dict["skin_response"],
            temperature=observation_dict["temperature"],
            activity_level=observation_dict["activity_level"],
            signal_quality=observation_dict["signal_quality"]
        )
        self.observations.append(obs)
        return True, "Observation added successfully."

    def get_observations(self) -> list[Observation]:
        """
        Get all observations in the session.
        """
        return self.observations

    def get_good_quality_observations(
        self,
        quality_threshold: float = 0.7,
    ) -> list[Observation]:
        """
        Get observations with signal quality at or above the threshold.
        """
        return [
            observation
            for observation in self.observations
            if is_good_signal_quality(observation.signal_quality, quality_threshold)
        ]

    