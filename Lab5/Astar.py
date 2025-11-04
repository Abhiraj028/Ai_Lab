import heapq

def Astar(graph, heuristic, start, end):
    path = {start: None}
    cost = {start: 0}
    frontier = [(heuristic[start], start)]

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == end:
            path_list = [current]
            while path[current] is not None:
                path_list.append(path[current])
                current = path[current]
            path_list.reverse()
            return path_list


        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                total = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (total, neighbor))
                path[neighbor] = current

    return None


if __name__ == "__main__":
    n, m = map(int, input("Enter number of nodes and edges: ").split())
    print("Enter node names:")
    nodes = input().split()  # e.g. A B C D

    print("Enter heuristic values for each node:")
    heuristic = {node: int(input(f"{node} =")) for node in nodes}

    graph = {node: {} for node in nodes}
    print("Enter edges and their costs (u v w):")
    for _ in range(m):
        u, v, w = input().split()
        graph[u][v] = int(w)

    start, end = nodes[0], nodes[-1]
    result = Astar(graph, heuristic, start, end)
    print("Result path:", result)
