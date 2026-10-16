import random

# THREE-ROOM CLEANING AGENT


# Ask the user for the condition of each room
rooms = {}

for room in ["A", "B", "C"]:
    condition = input(f"Is room {room} Dirty or Clean? ").capitalize()

    while condition not in ["Dirty", "Clean"]:
        condition = input(f"Please enter Dirty or Clean for room {room}: ").capitalize()

    rooms[room] = condition

# Agent starts in Room A
agent_position = "A"


# Display the current state of the rooms
def display_rooms():
    for room in ["A", "B", "C"]:
        if room == agent_position:
            print(f"[{room}-Agent]", end="  ")
        else:
            print(f"[{room}-{rooms[room]}]", end="  ")
    print()


# Ask how many steps the agent should run
steps = int(input("\nHow many steps should the agent run? "))

print("\nInitial State:")
display_rooms()

# Agent starts moving
for step in range(1, steps + 1):

    print(f"\nStep {step}:")
    display_rooms()

    # Find all dirty rooms
    dirty_rooms = [room for room in rooms if rooms[room] == "Dirty"]

    # Stop if all rooms are clean
    if not dirty_rooms:
        print("All rooms are clean. Agent is idle.")
        break

    # If the current room is dirty, clean it
    if rooms[agent_position] == "Dirty":
        rooms[agent_position] = "Clean"
        print(f"Room {agent_position} has been cleaned.")

    else:
        # Randomly choose another dirty room
        dirty_rooms = [room for room in rooms if rooms[room] == "Dirty"]

        if dirty_rooms:
            next_room = random.choice(dirty_rooms)
            print(f"Moving to room {next_room}")
            agent_position = next_room

    print("Current State:")
    display_rooms()


# Final result
print("\nFinal State:")
display_rooms()

if all(rooms[room] == "Clean" for room in rooms):
    print("All rooms are clean. Agent is idle.")
else:
    print("Agent stopped because the step limit was reached.")