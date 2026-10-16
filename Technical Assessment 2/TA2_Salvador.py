# Function to check if the current room is dirty
def is_dirty(environment, room):
    return environment[room] == "Dirty"


# Function to clean the current room
def clean_room(environment, room):
    environment[room] = "Clean"


# Get the initial condition of Room A and Room B
room_a = input("Is room A Dirty or Clean? ").capitalize()
room_b = input("Is room B Dirty or Clean? ").capitalize()

# Create the environment using a dictionary
environment = {
    "A": room_a,
    "B": room_b
}

print()

class Agent:
    def __init__(self):
        # The agent starts in Room A
        self.current_room = "A"

    # Method to move to the other room
    def move(self):
        if self.current_room == "A":
            self.current_room = "B"
        else:
            self.current_room = "A"

    # Perceive and act based on rules
    def perceive_and_act(self, environment):

        # Rule 1: If the current room is dirty, clean it
        if is_dirty(environment, self.current_room):
            clean_room(environment, self.current_room)
            return "Room " + self.current_room + " has been cleaned."

        # Rule 2: If the current room is clean, move to the other room
        else:
            old_room = self.current_room
            self.move()
            return "Moving to room " + self.current_room


# Ask the user how many steps the agent should run
steps = int(input("How many steps should the agent run? "))

print()

# Create the agent
agent = Agent()

# Run the simulation
for step in range(1, steps + 1):

    print("Step", step, ": Agent is in room", agent.current_room)

    # Agent perceives the environment and performs an action
    action = agent.perceive_and_act(environment)

    # Display the action
    print(action)

    # Display the current environment state
    print("Environment state:", environment)
    print()


input("Press any key to continue . . .")