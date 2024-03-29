# /bin/python3
# written by eyedi
# DFS algorithm in Python

# DFS algorithm, Recurrsive
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    #print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))


"""
Powered by ChatGPT 
"""

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited

# Example usage:
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(dfs(graph, 'A', []))