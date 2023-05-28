graph={'5':['3','7'],'3':['2','4'],'7':['8'],'2':[],'4':['8'],'8':[]}
node='5'
visit=set()
def bfs(graph,node):
    visited=[]
    queue=[]
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search")
bfs(graph,node)

def dfs(graph,node):
    if node not in visit:
        print(node, end=" ")
        visit.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor)
print("\nDepth First Search")
dfs(graph,node)