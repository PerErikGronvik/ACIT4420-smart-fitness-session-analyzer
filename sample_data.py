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
        "name": "John Doe",
        "age": 30,
        "gender": "male"
    }
    observations = [
        {
            "timestamp": "2024-06-01T08:00:00","heart_rate": 60,
            "skin_response": 0.5,
            "temperature": 36.5,
            "activity_level": 0,
            "signal_quality": 0.9
        },
        {
            "timestamp": "2024-06-01T08:05:00",
            "heart_rate": 62,
            "skin_response": 0.55,
            "temperature": 36.6,
            "activity_level": 0,
            "signal_quality": 0.9
        }
    ]
    return Participant, observations