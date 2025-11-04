def valid(state):
    # Check if missionaries on left bank are outnumbered by cannibals (and missionaries exist)
    if state[0][0] < state[0][1] and state[0][0] > 0:  # If left missionaries < left cannibals AND missionaries present
        return False  # Invalid state - missionaries would be eaten
    
    # Check if missionaries on right bank are outnumbered by cannibals (and missionaries exist)
    if state[1][0] < state[1][1] and state[1][0] > 0:  # If right missionaries < right cannibals AND missionaries present
        return False  # Invalid state - missionaries would be eaten
    
    return True  # State is valid - missionaries are safe on both banks


def successors(state):
    children = []  # Initialize empty list to store all valid successor states
    
    # Generate all possible boat combinations (i missionaries, j cannibals)
    for i in range(3):  # i = number of missionaries in boat (0, 1, or 2)
        for j in range(3):  # j = number of cannibals in boat (0, 1, or 2)
            # Boat capacity constraint: must have 1 or 2 people total (not 0, not 3+)
            if i + j < 1 or i + j > 2:  # If boat is empty or overloaded
                continue  # Skip this invalid combination
            
            # Generate new state based on boat position
            if state[2] == 1:  # If boat is on left bank (moving left → right)
                # Subtract from left bank, add to right bank, move boat to right (0)
                child = ((state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j), 0)
            else:  # If boat is on right bank (moving right → left)
                # Add to left bank, subtract from right bank, move boat to left (1)
                child = ((state[0][0] + i, state[0][1] + j), (state[1][0] - i, state[1][1] - j), 1)
            
            # Only add child state if it's valid (missionaries not outnumbered)
            if valid(child):  # Check safety constraints
                children.append(child)  # Add valid successor to list
    
    return children  # Return all valid successor states


def bfs(start, goal):
    visited = set()  # Track visited states to avoid cycles and redundant exploration
    queue = [[start]]  # Initialize queue with a path containing only the start state
    
    while queue:  # Continue until queue is empty (all paths explored)
        path = queue.pop(0)  # Dequeue first path (FIFO - breadth-first behavior)
        node = path[-1]  # Get the last state in the current path (frontier node)
        
        if node == goal:  # Goal test - check if we've reached the target state
            return path  # Return the complete path from start to goal
        
        # Explore all successors of the current node
        for child in successors(node):  # Generate all valid next states
            if child not in visited:  # Only explore unvisited states
                visited.add(child)  # Mark child as visited to prevent revisiting
                new_path = list(path)  # Create a copy of current path
                new_path.append(child)  # Extend path with new child state
                queue.append(new_path)  # Enqueue the extended path for future exploration
    
    return []  # No solution found - return empty list


# Custom input
print("Enter initial state:")
left_m = int(input("Left bank missionaries: "))  # Number of missionaries on left bank initially
left_c = int(input("Left bank cannibals: "))  # Number of cannibals on left bank initially
right_m = int(input("Right bank missionaries: "))  # Number of missionaries on right bank initially
right_c = int(input("Right bank cannibals: "))  # Number of cannibals on right bank initially
boat = int(input("Boat position (1=left, 0=right): "))  # Boat location (1=left bank, 0=right bank)
# State format: ((left_missionaries, left_cannibals), (right_missionaries, right_cannibals), boat_position)
initial = ((left_m, left_c), (right_m, right_c), boat)

print("\nEnter goal state:")
left_m = int(input("Left bank missionaries: "))  # Target missionaries on left bank
left_c = int(input("Left bank cannibals: "))  # Target cannibals on left bank
right_m = int(input("Right bank missionaries: "))  # Target missionaries on right bank
right_c = int(input("Right bank cannibals: "))  # Target cannibals on right bank
boat = int(input("Boat position (1=left, 0=right): "))  # Target boat position
goal = ((left_m, left_c), (right_m, right_c), boat)  # Construct goal state tuple

# Solve the missionaries and cannibals problem using BFS
path = bfs(initial, goal)  # Find shortest path from initial to goal state

# Display results
if path:  # If a solution exists
    for state in path:  # Print each state in the solution path
        print(state)
else:  # If no solution found
    print("No solution found.")