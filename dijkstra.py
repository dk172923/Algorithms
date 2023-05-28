def dijkstra(graph, start):
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0
    unvisited = set(graph.keys())
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: dist[vertex])
        unvisited.remove(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            new_distance = dist[current_vertex] + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
    
    return dist

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9}
}

start = 'A'
distances = dijkstra(graph, start)
print(distances)
