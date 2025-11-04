
def dfs(current_state, jug_sizes, target_volume, explored):
    jug1, jug2 = current_state  # Unpack current state into individual jug volumes
    
    # Base case: check if either jug contains the target volume
    if jug1 == target_volume or jug2 == target_volume:  # Goal test - target reached
        return [current_state]  # Return list containing only the goal state (end of path)

    explored.add(current_state)  # Mark current state as visited to avoid revisiting
    successors = get_successors(current_state, jug_sizes)  # Generate all possible next states from current state

    for successor in successors:  # Iterate through each possible next state
        if successor not in explored:  # Only explore states that haven't been visited yet
            path = dfs(successor, jug_sizes, target_volume, explored)  # Recursively search from successor state
            if path is not None:  # If recursive call found a path to the goal
                return [current_state] + path  # Prepend current state to path and return complete path
    
    return None  # No valid path found from this state (dead end, triggers backtracking)


def get_successors(state, jug_sizes):
    jug1, jug2 = state  # Unpack current volumes of both jugs
    jug1_cap, jug2_cap = jug_sizes  # Unpack maximum capacities of both jugs
    successors = []  # Initialize empty list to store all possible successor states

    # Generate all 6 possible actions from current state:
    successors.append((jug1_cap, jug2))  # Action 1: Fill jug1 to capacity (ignore current jug1 volume)
    successors.append((jug1, jug2_cap))  # Action 2: Fill jug2 to capacity (ignore current jug2 volume)
    successors.append((0, jug2))         # Action 3: Empty jug1 completely (set to 0)
    successors.append((jug1, 0))         # Action 4: Empty jug2 completely (set to 0)

    # Action 5: Pour jug1 -> jug2
    amount_to_pour = min(jug1, jug2_cap - jug2)  # Calculate max pourable: limited by jug1 content or jug2 space
    successors.append((jug1 - amount_to_pour, jug2 + amount_to_pour))  # Update both jugs after pouring

    # Action 6: Pour jug2 -> jug1
    amount_to_pour = min(jug2, jug1_cap - jug1)  # Calculate max pourable: limited by jug2 content or jug1 space
    successors.append((jug1 + amount_to_pour, jug2 - amount_to_pour))  # Update both jugs after pouring

    # Filter successors to only include valid states (within capacity constraints)
    return [s for s in successors if is_valid_state(s, jug_sizes)]  # List comprehension filters invalid states


def is_valid_state(state, jug_sizes):
    jug1_cap, jug2_cap = jug_sizes  # Unpack maximum capacities
    jug1, jug2 = state  # Unpack volumes in proposed state
    # Validate that both jug volumes are non-negative and within their respective capacities
    return 0 <= jug1 <= jug1_cap and 0 <= jug2 <= jug2_cap  # Return True only if both constraints satisfied


# ---- Custom Input ----
jug1_size = int(input("Enter size of jug 1: "))  # Prompt user and convert input to integer for jug1 capacity
jug2_size = int(input("Enter size of jug 2: "))  # Prompt user and convert input to integer for jug2 capacity
target = int(input("Enter target volume: "))  # Prompt user for desired target volume to achieve
explored = set()
# Solve the water jug problem using DFS, starting from empty jugs (0, 0)
path = dfs((0,0), (jug1_size,jug2_size), target, explored)  # Call solver with capacities, target, and initial state

print("\nDFS Solution Path:")  # Print header for solution output
print(path)  # Display the sequence of states from start to goal (or None if impossible)