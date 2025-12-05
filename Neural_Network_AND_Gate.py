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

# Re-initialize weights/bias to random
weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
bias = random.uniform(-1, 1)
learning_rate = 0.1

def activation_function(z):
    return 1 if z > 0 else 0

print(f"Target: AND Gate Logic")
print(f"Initial Random Weights: {weights}")
print("-" * 30)

for epoch in range(20):
    total_error = 0
    for data in training_data:
        inputs = data['inputs']
        target = data['label']
        
        # Forward Pass
        weighted_sum = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + bias
        prediction = activation_function(weighted_sum)

        # Error & Update
        error = target - prediction 
        total_error += abs(error)
        
        if error != 0:
            weights[0] += learning_rate * error * inputs[0]
            weights[1] += learning_rate * error * inputs[1]
            bias += learning_rate * error

            