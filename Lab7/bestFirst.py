import heapq

def best_first_search(graph, heuristic, start, end):
    path = {start: None}
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
            if neighbor not in path:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
                path[neighbor] = current
    return None


if __name__ == "__main__":
    n, m = map(int, input("Enter number of nodes and edges: ").split())
    print("Enter node names:")
    nodes = input().split()  # e.g. A B C D

    print("Enter heuristic values for each node:")
    heuristic = {node: int(input(f"h({node}) = ")) for node in nodes}

    graph = {node: {} for node in nodes}
    print("Enter edges and their costs (u v w):")
    for _ in range(m):
        u, v, w = input().split()
        graph[u][v] = int(w)

    start, end = nodes[0], nodes[-1]
    result = best_first_search(graph, heuristic, start, end)
    print("Result path:", result)
