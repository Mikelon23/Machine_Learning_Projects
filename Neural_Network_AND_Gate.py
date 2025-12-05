import random

# Set seed for reproducibility
random.seed(42)

# EXPERIMENT: CHANGING THE DATA TO AN 'AND' GATE
# Notice: The code logic (Algorithm) remains exactly the same. 
# We only change the Data (The Fuel).
# AND Logic: Output 1 only if BOTH inputs are 1.
training_data = [
    {'inputs': [0, 0], 'label': 0},
    {'inputs': [0, 1], 'label': 0}, # Changed from 1 to 0
    {'inputs': [1, 0], 'label': 0}, # Changed from 1 to 0
    {'inputs': [1, 1], 'label': 1},
]

