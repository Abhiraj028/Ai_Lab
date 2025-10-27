def valid(state):
    if state[0][0] < state[0][1] and state[0][0] > 0:
        return False
    if state[1][0] < state[1][1] and state[1][0] > 0:
        return False
    return True


def successors(state):
    children = []
    for i in range(3):
        for j in range(3):
            if i + j < 1 or i + j > 2:
                continue
            if state[2] == 1:
                child = ((state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j), 0)
            else:
                child = ((state[0][0] + i, state[0][1] + j), (state[1][0] - i, state[1][1] - j), 1)
            if valid(child):
                children.append(child)
    return children


def bfs(start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for child in successors(node):
            if child not in visited:
                visited.add(child)
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)
    return []


# Custom input
print("Enter initial state:")
left_m = int(input("Left bank missionaries: "))
left_c = int(input("Left bank cannibals: "))
right_m = int(input("Right bank missionaries: "))
right_c = int(input("Right bank cannibals: "))
boat = int(input("Boat position (1=left, 0=right): "))
initial = ((left_m, left_c), (right_m, right_c), boat)

print("\nEnter goal state:")
left_m = int(input("Left bank missionaries: "))
left_c = int(input("Left bank cannibals: "))
right_m = int(input("Right bank missionaries: "))
right_c = int(input("Right bank cannibals: "))
boat = int(input("Boat position (1=left, 0=right): "))
goal = ((left_m, left_c), (right_m, right_c), boat)

path = bfs(initial, goal)
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")