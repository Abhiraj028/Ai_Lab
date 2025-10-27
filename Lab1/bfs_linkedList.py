from collections import deque

class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def bfs_linked(graph, node, visitedArr):
    queue = deque([node])
    visitedArr[node] = True

    while queue:
        node = queue.popleft()
        print(node + 1, end=" ")

        temp = (graph[node])
        while temp:
            if not visitedArr[temp.data]:
                queue.append(temp.data)
                visitedArr[temp.data] = True
            temp = temp.next

def main():
    nodes = int(input("Enter the number of nodes in the graph: "))

    graph = []
    for _ in range(nodes):
        graph.append(None)

    edges = int(input("Enter the total number of edges in the graph: "))
    print("Enter the edges (u v):")

    for _ in range(edges):
        num= input().strip().split()
        u = int(num[0]) - 1
        v = int(num[1]) - 1

        node = AdjNode(v)
        node.next = graph[u]
        graph[u] = node

        node = AdjNode(u)
        node.next = graph[v]
        graph[v] = node

    visitedArr = [False] * nodes

    for node in range(nodes):
        if not visitedArr[node]:
            bfs_linked(graph, node, visitedArr)

if __name__ == "__main__":
    main()
