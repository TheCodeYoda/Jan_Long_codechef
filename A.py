t=int(input())

for _ in range(t):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    su=sum(a)
    ans=su//k
    print(min(ans,d))

