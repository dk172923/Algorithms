def floyd(graph):
    n=len(graph)
    dist=[[float('inf')for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j]=0
            else:
                dist[i][j]=graph[i][j]
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                intermediate_distance=dist[i][k]+dist[k][j]
                if dist[i][j]>intermediate_distance:
                    dist[i][j]=intermediate_distance
    return dist
    
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]
output = floyd(graph)
print(output)