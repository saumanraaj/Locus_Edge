import json
import random

# Define possible commands and parameters
directions = ["forward", "backward", "left", "right"]
angles = [15, 30, 45, 60, 90, 120, 180, 270, 360]
distances = [0.5, 1, 2, 3, 5, 10]
special_commands = [
    "Stop the robot.",
    "Rotate 360 degrees clockwise.",
    "Move diagonally forward-left by 1 meter.",
    "Move diagonally backward-right by 2 meters."
]

# Function to create a single input-output pair
def generate_command():
    if random.random() < 0.2:  # 20% chance of special commands
        command = random.choice(special_commands)
        if "Stop" in command:
            return {
                "input": command,
                "output": '{"x": 0, "y": 0, "yaw": 0}'
            }
        elif "360 degrees clockwise" in command:
            return {
                "input": command,
                "output": '{"x": 0, "y": 0, "yaw": -6.2832}'
            }
        elif "diagonally forward-left" in command:
            return {
                "input": command,
                "output": '{"x": 0.707, "y": 0.707, "yaw": 0}'
            }
        elif "diagonally backward-right" in command:
            return {
                "input": command,
                "output": '{"x": -1.414, "y": -1.414, "yaw": 0}'
            }
    else:
        action = random.choice(["Move", "Rotate"])
        if action == "Move":
            direction = random.choice(directions)
            distance = random.choice(distances)
            if direction == "forward":
                return {
                    "input": f"Move {direction} by {distance} meters.",
                    "output": f'{{"x": {distance}, "y": 0, "yaw": 0}}'
                }
            elif direction == "backward":
                return {
                    "input": f"Move {direction} by {distance} meters.",
                    "output": f'{{"x": {-distance}, "y": 0, "yaw": 0}}'
                }
            elif direction == "left":
                return {
                    "input": f"Move {direction} by {distance} meters.",
                    "output": f'{{"x": 0, "y": {distance}, "yaw": 0}}'
                }
            elif direction == "right":
                return {
                    "input": f"Move {direction} by {distance} meters.",
                    "output": f'{{"x": 0, "y": {-distance}, "yaw": 0}}'
                }
        elif action == "Rotate":
            direction = random.choice(["left", "right"])
            angle = random.choice(angles)
            yaw = angle * 3.1416 / 180  # Convert degrees to radians
            yaw = yaw if direction == "left" else -yaw
            return {
                "input": f"Rotate {direction} by {angle} degrees.",
                "output": f'{{"x": 0, "y": 0, "yaw": {yaw:.4f}}}'
            }

# Generate 10,000 examples
data = [generate_command() for _ in range(10000)]

# Save to a JSON file
output_file = "dataset.json"
with open(output_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Dataset with {len(data)} examples saved to {output_file}.")
