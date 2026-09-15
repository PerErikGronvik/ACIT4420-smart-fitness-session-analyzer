# %% [markdown]
# Smart Fitness Session Analyzer Report
# To run the file Install the VS Code Python and Jupyter extensions and open this file in VS Code. and the ipykernel package must be installed beforehand.

# %% [markdown]
## Create a session

# %%
from src.observation import Observation
from src.participant import Participant
from src.session import Session

participant = Participant("John Doe", 70, 0.5)
session = Session(participant)

observation_data = {
    "timestamp": 1,
    "heart_rate": 70,
    "skin_response": 0.5,
    "temperature": 36.6,
    "activity_level": 0.8,
    "signal_quality": 0.9,
}

success, message = session.add_observation(observation_data)
assert success
print(message)

# %% [markdown]
## Check one observation

# %%
observations = session.get_observations()
assert len(observations) == 1

observation = observations[0]
assert isinstance(observation, Observation)
assert observation.to_dict() == observation_data
print(observation)

# %% [markdown]
## Create a session summary

# %%
summary = session.get_session_summary()

assert summary["total_observations"] == 1
assert summary["good_quality_observations"] == 1
assert summary["average_heart_rate"] == 70
assert summary["min_heart_rate"] == 70
assert summary["max_heart_rate"] == 70
assert summary["average_activity_level"] == 0.8
assert summary["average_temperature"] == 36.6

for name, value in summary.items():
    print(f"{name}: {value}")

# %% [markdown]
# # Test of 5 required scenarios

# %%
from sample_data import get_resting_session_data
