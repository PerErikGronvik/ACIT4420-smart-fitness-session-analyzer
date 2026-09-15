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

def test_participant_invalid_values():
    try:
        p = Participant("Ola Normann", 25, 0.5)
    except ValueError as e:
        assert str(e) == "Resting heart rate must be between 30 and 120."
    else:
        raise AssertionError("Expected invalid resting heart rate to raise ValueError")

    try:
        p = Participant("Ola Normann", 60, 1)
        p.resting_activity_level = 1.5
    except ValueError as e:
        assert str(e) == "Resting activity level must be between 0.0 and 1.0."
    else:
        raise AssertionError("Expected invalid activity level to raise ValueError")

def test_observation():
    from src.observation import Observation
    o = Observation(1234567890, 70, 0.5, 36.6, 0.8, 0.9)
    assert o.timestamp == 1234567890
    assert o.heart_rate == 70
    assert o.skin_response == 0.5
    assert o.temperature == 36.6
    assert o.activity_level == 0.8
    assert o.signal_quality == 0.9
    
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

def test_calculations():
    from src.calculations import (
        calculate_average,
        calculate_min,
        calculate_max,
        calculate_hr_elevation,
        detect_recovery,
    )

    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert calculate_average(values) == 3.0
    assert calculate_min(values) == 1.0
    assert calculate_max(values) == 5.0

    assert calculate_hr_elevation(80, 60) == 20

    from src.observation import Observation
    observations = [
        Observation(1, 80, 0.5, 36.6, 0.8, 0.9),
        Observation(2, 78, 0.5, 36.6, 0.7, 0.9),
        Observation(3, 76, 0.5, 36.6, 0.6, 0.9),
        Observation(4, 74, 0.5, 36.6, 0.5, 0.9),
        Observation(5, 72, 0.5, 36.6, 0.4, 0.9),
        Observation(6, 70, 0.5, 36.6, 0.3, 0.9),
        Observation(7, 68, 0.5, 36.6, 0.2, 0.9),
        Observation(8, 66, 0.5, 36.6, 0.1, 0.9),
    ]
    assert detect_recovery(observations, 60) is True

def test_session():
    from src.session import Session
    from src.participant import Participant

    participant = Participant("John Doe", 70, 0.5)
    session = Session(participant)

    observation_dict = {
        "timestamp": 1234567890,
        "heart_rate": 70,
        "skin_response": 0.5,
        "temperature": 36.6,
        "activity_level": 0.8,
        "signal_quality": 0.9
    }
    success, message = session.add_observation(observation_dict)
    assert success
    assert message == "Observation added successfully."
    observations = session.get_observations()
    assert len(observations) == 1
    obs = observations[0]
    assert obs.timestamp == 1234567890
    assert obs.heart_rate == 70
    assert obs.skin_response == 0.5
    assert obs.temperature == 36.6
    assert obs.activity_level == 0.8
    assert obs.signal_quality == 0.9

if __name__ == "__main__":
    tests = [
        test_participant,
        test_participant_invalid_values,
        test_observation,
        test_validation,
        test_calculations,
        test_session,
    ]

    passed = 0
    for test in tests:
        try:
            test()
        except AssertionError as error:
            print(f"FAIL  {test.__name__}: {error}")
        except Exception as error:
            print(f"ERROR {test.__name__}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"PASS  {test.__name__}")

    print(f"\n{passed}/{len(tests)} tests passed")
    if passed != len(tests):
        raise SystemExit(1)