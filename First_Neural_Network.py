import random

# 1. The Data (The Fuel) - OR Gate Logic
# This defines the reality we want the machine to learn.
training_data = [
    {'inputs': [0, 0], 'label': 0},
    {'inputs': [0, 1], 'label': 1},
    {'inputs': [1, 0], 'label': 1},
    {'inputs': [1, 1], 'label': 1},
]

# 2. The Model Parameters (The Engine)
# We start with random weights because the machine "knows nothing" yet.
weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
bias = random.uniform(-1, 1)
learning_rate = 0.1 # The size of the "step" we take to correct errors

def activation_function(z):
    """Step function: Fire (1) if z > 0, else Silence (0)"""
    return 1 if z > 0 else 0

# 3. The Training Loop (The Learning Process)
epochs = 20 # How many times we iterate through the entire dataset

print(f"Initial Random Weights: {weights}")
print(f"Initial Random Bias: {bias}")
print("-" * 30)

for epoch in range(epochs):
    total_error = 0
    for data in training_data:
        inputs = data['inputs']
        target = data['label']

        # A. Forward Pass (The Attempt)
        # Formula: z = (x1 * w1) + (x2 * w2) + b
        weighted_sum = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + bias
        prediction = activation_function(weighted_sum)

        # B. Calculate Error (The Feedback)
        