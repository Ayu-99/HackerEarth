# Write your code here
from collections import defaultdict
d=defaultdict(list)
dist=[0]*10001


def bfs(src):
    queue=[]*10001
    vis=[False]*10001
    queue.append(src)
    vis[src]=True
    dist[src]=0

    while queue:
        root=queue[0]
        queue.pop(0)

        for i in range(len(d[root])):
            x=d[root]

            if not vis[x[i]]:
                queue.append(x[i])
                dist[x[i]]=dist[root]+1
                vis[x[i]]=True

def countNodes(node,t, n): # node, distance, no of nodes
    
    bfs(node)
    count=0
    for i in range(len(dist)):
        if dist[i]==t:
            count+=1

    return count        

def main():
    n,e=map(int, (input().split()))
    
    for i in range(e):
        u,v=map(int, input().split())
        d[u].append(v)
        d[v].append(u)

    m=int(input()) # no of queries
    for i in range(m):
        node, t=map(int, input().split())
        print(countNodes(node,t,n))


if __name__=="__main__":
    main()
