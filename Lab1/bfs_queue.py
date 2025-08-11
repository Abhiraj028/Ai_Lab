from collections import deque


def bfs_queue(graph,node,visitedArr):
    queue = deque([node])
    visitedArr[node] = True

    while queue:
        node = queue.popleft()
        print(node + 1, end = " ")

        for adj in graph[node]:
            if not visitedArr[adj]:
                queue.append(adj)
                visitedArr[adj] = True


def main():
    nodes = int(input("Enter the number of nodes in the graph: "))
    graph = {}
    for node in range(nodes):
        graph[node] = []

    edges = int(input("Enter the total number of edges in the graph:"))
    print("Enter the edges (u - v once):")

    for _ in range(edges):
        num = input().strip().split()
        u = int(num[0]) - 1
        v = int(num[1]) - 1

        graph[u].append(v)
        graph[v].append(u)

    visitedArr = [False] * nodes

    for node in range(nodes):
        if not visitedArr[node]:
            bfs_queue(graph,node,visitedArr)

if __name__ == "__main__":
    main()