import heapq

def best_first_search(graph, heuristic, start, end):
    path = {start: None}
    frontier = [(heuristic[start], start)]
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == end:
            path_list = [current]
            while path[current] is not None:
                path_list.append(path[current])
                current = path[current]
            path_list.reverse()
            return path_list

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in path:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
                path[neighbor] = current
    return None

if __name__ == "__main__":
    nodes_length = int(input("Enter the number of nodes:"))
    edges = int(input("Enter the total number of edges:"))
    nodes = []
    print("Enter names for the nodes")
    for n in range(nodes_length):
        nodes.append(input())
    heuristic = {}
    print("Enter the heuristic costs for the nodes")
    for n in nodes:
        heuristic[n] = int(input())
    graph = {n: {} for n in nodes}
    print("Add edges and their costs: ")
    for _ in range(edges):
        start = input("Start Node: ")
        end = input("End Node: ")
        cost = int(input("Edge Cost: "))
        graph[start][end] = cost

    answer_path = best_first_search(graph, heuristic, nodes[0], nodes[-1])
    print("Result is: ", answer_path)