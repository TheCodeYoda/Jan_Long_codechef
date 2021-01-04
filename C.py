t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    su_a=sum(a)
    su_b=sum(b)
    if(su_a>su_b):
        print(0)
    else:
        c=0
        for i in range(min(n,m)):
            if(b[i]>a[i]):
                su_a=su_a-a[i]+b[i]
                su_b=su_b-b[i]+a[i]
                c+=1
                if(su_a>su_b):
                    print(c)
                    break
        if(su_a<=su_b):
            print(-1)
