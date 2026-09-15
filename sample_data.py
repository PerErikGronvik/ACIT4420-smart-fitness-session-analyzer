"""
Sample data for testing the fitness session analyzer.

Data to demonstrate the five required scenarios:
1. Resting state
2. Moderate activity
3. High activity
4. Activity followed by recovery
5. Poor quality or invalid sensor data

"""

def get_resting_session_data():
    Participant = {
        "id": 1,
        "name": "Resting Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {   "timestamp": "2024-06-01T08:00:00", "heart_rate": 60, "skin_response": 0.5, "temperature": 36.5, "activity_level": 0, "signal_quality": 0.9 },

    ]
    return Participant, observations

def get_moderate_activity_session_data():
    Participant = {
        "id": 2,
        "name": "Moderate Activity Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {   "timestamp": "2024-06-01T08:00:00", "heart_rate": 60, "skin_response": 0.5, "temperature": 36.5, "activity_level": 0, "signal_quality": 0.9 },

    ]
    return Participant, observations

def get_high_activity_session_data():
    Participant = {
        "id": 3,
        "name": "High Activity Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {   "timestamp": "2024-06-01T08:00:00", "heart_rate": 60, "skin_response": 0.5, "temperature": 36.5, "activity_level": 0, "signal_quality": 0.9 },

    ]
    return Participant, observations

def get_poor_quality_session_data():
    Participant = {
        "id": 4,
        "name": "Poor Quality Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {   "timestamp": "2024-06-01T08:00:00", "heart_rate": 60, "skin_response": 0.5, "temperature": 36.5, "activity_level": 0, "signal_quality": 0.9 },

    ]
    return Participant, observations

def get_activity_followed_by_recovery_session_data():
    Participant = {
        "id": 5,
        "name": "Activity Followed by Recovery Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {   "timestamp": "2024-06-01T08:00:00", "heart_rate": 60, "skin_response": 0.5, "temperature": 36.5, "activity_level": 0, "signal_quality": 0.9 },

    ]
    return Participant, observations