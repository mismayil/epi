from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_recursive(self, visited, queue):
        if queue:
            s = queue.pop(0)
            print(s, end=' ')

            for v in self.graph[s]:
                if v not in visited:
                    queue.append(v)
                    visited.append(v)

            self.bfs_recursive(visited, queue)


    def bfs(self, s, recursive=False):
        if recursive: return self.bfs_recursive([s] ,[s])

        visited = [s]
        queue = [s]

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for v in self.graph[s]:
                if v not in visited:
                    queue.append(v)
                    visited.append(v)

    def dfs_recursive(self, s, visited):
        visited.append(s)
        print(s, end=' ')

        for v in self.graph[s]:
            if v not in visited:
                self.dfs_recursive(v, visited)

    def dfs(self, s, recursive=False):
        if recursive: return self.dfs_recursive(s, [])

        visited = [s]
        stack = [s]

        while stack:
            s = stack.pop()
            print(s, end=' ')

            for v in self.graph[s]:
                if v not in visited:
                    stack.append(v)
                    visited.append(v)


graph = Graph()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('c', 'e')
graph.add_edge('e', 'd')
graph.add_edge('d', 'c')
graph.add_edge('b', 'k')
graph.add_edge('k', 'i')
graph.add_edge('d', 'h')
graph.add_edge('f', 'g')
graph.add_edge('g', 'h')
graph.add_edge('i', 'j')
graph.add_edge('j', 'l')
graph.add_edge('l', 'i')

graph.dfs('a')
