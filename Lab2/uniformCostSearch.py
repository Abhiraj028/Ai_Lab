from queue import PriorityQueue

def uniform_cost_search(start_node, goal_node, graph):
    pQ = PriorityQueue()
    pQ.put((0, start_node))
    explored = set()

    while not pQ.empty():
        current_cost, current_node = pQ.get()

        if current_node == goal_node:
            return current_cost

        if current_node in explored:
            continue

        explored.add(current_node)

        for neighbor, cost in graph.get(current_node, {}).items():
            if neighbor not in explored:
                new_cost = current_cost + cost
                pQ.put((new_cost, neighbor))

    return -1

def get_graph_input():
    graph = {}
    num_nodes = int(input("Enter number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        graph[node] = {}
        num_neighbors = int(input(f"Enter number of neighbors for {node}: "))
        for _ in range(num_neighbors):
            neighbor = input("  Enter neighbor name: ")
            cost = int(input(f"  Enter cost to {neighbor}: "))
            graph[node][neighbor] = cost
    return graph

if __name__ == "__main__":
    print("Uniform Cost Search - Interactive Mode")
    graph = get_graph_input()
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")

    cost = uniform_cost_search(start_node, goal_node, graph)
    if cost != -1:
        print(f"Least cost from {start_node} to {goal_node} is: {cost}")
    else:
        print("No path found to the goal node.")
