from src.participant import Participant

def test_participant():
    p = Participant("Ola Normann", 60, 0.5)
    assert p.name == "Ola Normann"
    assert p.resting_heart_rate == 60
    assert p.resting_activity_level == 0.5

    p.resting_heart_rate = 70
    assert p.resting_heart_rate == 70

    p.resting_activity_level = 0.8
    assert p.resting_activity_level == 0.8

    print(p)

def test_participant_invalid_values():
    try:
        p = Participant("Ola Normann", 25, 0.5)
    except ValueError as e:
        assert str(e) == "Resting heart rate must be between 30 and 120."

    try:
        p = Participant("Ola Normann", 60, 1)
        p.resting_activity_level = 1.5
    except ValueError as e:
        assert str(e) == "Resting activity level must be between 0.0 and 1.0."
def test_observation():
    from src.observation import Observation
    o = Observation(1234567890, 70, 0.5, 36.6, 0.8, 0.9)
    assert o.timestamp == 1234567890
    assert o.heart_rate == 70
    assert o.skin_response == 0.5
    assert o.temperature == 36.6
    assert o.activity_level == 0.8
    assert o.signal_quality == 0.9

    print(o)
    
def test_validation():
    from src.validation import validate_observation, is_good_signal_quality

    observation = {
        "timestamp": 1234567890,
        "heart_rate": 70,
        "skin_response": 0.5,
        "temperature": 36.6,
        "activity_level": 0.8,
        "signal_quality": 0.9
    }
    bad_observation = {
        "timestamp": 1234567890,
        "heart_rate": 25,
        "skin_response": 1.5,
        "temperature": 50.0,
        "activity_level": -0.1,
        "signal_quality": 1.5
    }
    is_valid, error_message = validate_observation(observation)
    assert is_valid
    assert error_message == ""

    is_valid, error_message = validate_observation(bad_observation)
    assert not is_valid
    assert error_message == "Heart rate must be between 30 and 230."

    # Test signal quality threshold
    assert not is_good_signal_quality(bad_observation["signal_quality"])

    assert is_good_signal_quality(observation["signal_quality"])


if __name__ == "__main__":
    test_participant()
    test_participant_invalid_values()
    test_observation()
    test_validation()