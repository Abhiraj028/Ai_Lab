def dfs_stack(graph,start,visitedArr):
    stack = [start]
    while stack:
        popped = stack.pop()

        if visitedArr[popped]:
            continue
            
        visitedArr[popped] = True
        print(popped+1, end=" ")

        for adj in graph[popped]:
            if not visitedArr[adj]:
                stack.append(adj)


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
            dfs_stack(graph,node,visitedArr)

if __name__ == "__main__":
    main()