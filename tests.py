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


if __name__ == "__main__":
    test_participant()
    test_participant_invalid_values()