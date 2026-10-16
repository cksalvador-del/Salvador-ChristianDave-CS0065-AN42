import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Get user input from console --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# -------- Agent Definition --------
class RandomWalker(ap.Agent):

    def setup(self):
        self.position = (0, 0)
        self.path = []

    def step(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        x, y = self.position

        # Try to move to a new position
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            # Keep agents inside the grid
            if (0 <= new_x < self.model.p.grid_size[0] and
                    0 <= new_y < self.model.p.grid_size[1]):

                new_position = (new_x, new_y)

                # Avoid other agents
                occupied = False

                for other in self.model.agents:
                    if other != self and other.position == new_position:
                        occupied = True
                        break

                if not occupied:
                    self.position = new_position
                    break

        # Record the position in the path
        self.path.append(self.position)

# -------- Model Definition --------
class RandomWalkModel(ap.Model):

    def setup(self):

        # Create agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        # Initialize random positions
        positions = []

        for agent in self.agents:

            # Find an unoccupied starting position
            while True:
                position = (
                    random.randint(0, self.p.grid_size[0] - 1),
                    random.randint(0, self.p.grid_size[1] - 1)
                )

                if position not in positions:
                    positions.append(position)
                    break

            agent.position = position
            agent.path = [position]

        # Create grid
        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()

# -------- Parameters from user input --------
parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps
}

# -------- Run Model --------
model = RandomWalkModel(parameters)
model.setup()

# -------- Interactive Animation --------
fig, ax = plt.subplots()

ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)

ax.set_xticks(range(model.p.grid_size[0]))
ax.set_yticks(range(model.p.grid_size[1]))

ax.grid(True)

# -------- Create lines for agent paths --------
path_lines = []

for agent in model.agents:
    line, = ax.plot([], [], linewidth=1)
    path_lines.append(line)

# -------- Create agent dots --------
scat = ax.scatter([], [], s=200)

# -------- Animation Update --------
def update(frame):

    # Move agents
    model.step()

    # Update agent positions
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    scat.set_offsets(list(zip(x, y)))

    # Update paths
    for i, agent in enumerate(model.agents):

        path_x = [position[0] for position in agent.path]
        path_y = [position[1] for position in agent.path]

        path_lines[i].set_data(path_x, path_y)

    return [scat] + path_lines

# -------- Run Animation --------
ani = animation.FuncAnimation(
    fig,
    update,
    frames=model.p.steps,
    blit=True,
    repeat=False
)

plt.title("Random Walker Simulation with Agent Paths")
plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.show()

# -------- Display Final Positions --------
print("\nFinal Positions of Agents:")

for i, agent in enumerate(model.agents):
    print(
        f"Agent {i + 1}: "
        f"({agent.position[0]}, {agent.position[1]})"
    )

# -------- Analyze Distribution --------
print("\nFinal Position Distribution:")

position_count = {}

for agent in model.agents:

    position = agent.position

    if position in position_count:
        position_count[position] += 1
    else:
        position_count[position] = 1

for position, count in position_count.items():

    print(
        f"Position {position}: "
        f"{count} agent(s)"
    )

