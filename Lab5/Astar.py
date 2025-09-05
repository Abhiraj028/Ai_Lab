import heapq

def Astar(graph, heuristic, start, end):
    path = {start: None}
    cost = {start: 0}
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
            new_cost = cost[current] + graph[current][neighbor]   #f(n)
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                total = new_cost + heuristic[neighbor]
                heapq.heappush(frontier,(total,neighbor))
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
    print("Enter the hueristic costs for the nodes")
    for n in nodes:
        heuristic[n] = int(input())
    graph = {n: {} for n in nodes}
    print("Add edges and their costs: ")
    for _ in range(edges):
        start = input("Start Node: ")
        end = input("End Node: ")
        cost = int(input("Edge Cost: "))
        graph[start][end] = cost

    answer_path = Astar(graph,heuristic,nodes[0],nodes[-1])
    print("Result is: ",answer_path)

