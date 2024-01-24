# Using a Python dictionary to act as an adjacency list
graph = {
  '1' : ['2', '3'],
  '2' : ['1', '3', '4'],
  '3' : ['1', '2', '5'],
  '4' : ['2', '5', '6', '7'],
  '5' : ['3', '4'],
  '7' : ['4'],
  '6' : ['4']
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("the DFS of given graph with root - 1 : \n")
dfs(visited, graph, '1')