from queue import PriorityQueue

def uniform_cost_search(graph, start, end):
    pQ = PriorityQueue()
    pQ.put((0, start))
    explored = set()

    while not pQ.empty():
        current_cost, current_node = pQ.get()

        if current_node == end:
            return current_cost

        if current_node in explored:
            continue

        explored.add(current_node)
        
        for neighbor in graph[current_node]:
            cost = graph[current_node][neighbor] 
            if neighbor not in explored:
                new_cost = current_cost + cost
                pQ.put((new_cost, neighbor))
    return -1


if __name__ == "__main__":
    n, m = map(int, input("Enter number of nodes and edges: ").split())
    print("Enter node names:")
    nodes = input().split()  # e.g. A B C D

    graph = {node: {} for node in nodes}
    print("Enter edges and their costs (u v w):")
    for _ in range(m):
        u, v, w = input().split()
        graph[u][v] = int(w)

    start, end = nodes[0], nodes[-1]
    cost = uniform_cost_search(graph, start, end)
    print(f"Least cost from {start} to {end} is: {cost}")
