def warshall(graph):
    n=len(graph)
    closure=[[0 for i in range(n)]for j in range(n)]
    closure=graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j]=closure[i][j] or (closure[i][k] and closure[k][j])
    return closure
graph=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
result=warshall(graph)
print(result)