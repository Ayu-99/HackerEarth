# Write your code here
from collections import defaultdict
d=defaultdict(list)
glives=[]
poss=[]
dis=[0]*10001
vis=[False]*10001

def girlChosen(src,l):

   
    dis[src]=l
    vis[src]=True

    for i in range(len(d[src])):
        
        if not vis[d[src][i]]:
            girlChosen(d[src][i], l+1)
        


def main():
    n=int(input())
    for i in range(n-1):
        u,v=map(int, input().split())
        d[u].append(v)

    
    

    girlChosen(1,0)
    # print(min(poss))
    q=int(input())
    m=float("inf")
    for i in range(q):
    
        x=int(input())
        if dis[x]<m:
            if x<m:
                m=x
    print(m)

if __name__=="__main__":
   #main
    main()
