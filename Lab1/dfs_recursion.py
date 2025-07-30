def dfs_recursive(graph,node,visitedArr):
    visitedArr[node] = True
    print(node+1, end=" ")

    for adj in graph[node]:
        if not visitedArr[adj]:
            dfs_recursive(graph,adj,visitedArr)


def main():
    nodes = int(input("Enter the number of nodes in the graph: "))
    edges = int(input("Enter the total number of edges in the graph: "))
    graph = {}

    for node in range(nodes):
        graph[node] = []

    print("Enter the nodes for the edges(u to v once): ")

    for _ in range(edges):
        num = input().split()
        u = int(num[0]) - 1
        v = int(num[1]) - 1

        graph[u].append(v)
        graph[v].append(u)

    visitedArr = [False] * nodes

    for node in range(nodes):
        if not visitedArr[node]:
            dfs_recursive(graph,node,visitedArr)

if __name__ == "__main__":
    main()