# Write your code here
from collections import defaultdict
d=defaultdict(list)
path=[]
queue=[]*10001
vis=[False]*10001
prev=[0]*10001
dis=[1]*10001

def bfs(src,des, t, c):

    

    queue.append(src)
    vis[src]=True
    # path.append(src)
    while queue:
        root=queue[0]
        queue.pop(0)

        # path.append(root)
        # cost+=c+(t-c)
        # if root==des:
        #     break
        for i in range(len(d[root])):
            x=d[root]
            if not vis[x[i]]:
                queue.append(x[i])
                vis[x[i]]=True
                prev[x[i]]=root
                dis[x[i]]=dis[root]+1


def main():

    n,m,t,c=map(int, input().split())
    for i in range(m):
        u,v=map(int,input().split())
        d[u].append(v)
        d[v].append(u)

    for i in range(1,n+1):
        d[i].sort()

    x,y=map(int,input().split())
    bfs(x,y, t, c)
    print(dis[y])
    path=[str(y)]
    now=y
    while now!=x:
        path.append(str(prev[now]))
        now=prev[now]
    print(' '.join( (path[::-1])))
    # print(' '.join(path))

    # print(path)
if __name__ == "__main__":
    main()
