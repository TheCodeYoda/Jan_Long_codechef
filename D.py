t=int(input())

for _ in range(t):
    n,k,x,y=map(int,input().split())
    flag=0
    if(y>x):
        flag=1
    t_x=max(x,y)
    t_y=min(x,y)
    x=t_x
    y=t_y
    l=[]
    if(x==y):
        print(n,n)
    else:
        m1=min(n-x,n-y)
        x,y=x+m1,y+m1
        l.append((x,y))
        for _ in range(3):
            if(x==n):
                x=x-(n-y)
                y=n
                l.append((x,y))
            elif(y==n):
                y=y-x
                x=0
                l.append((x,y))
            elif(x==0):
                x=x+y
                y=0
                l.append((x,y))
            elif(y==0):
                y=y+(n-x)
                x=n
                l.append((x,y))
    
        ans=l[(k%4)-1]
        #print(l)
        if(flag):
            print(ans[1],ans[0])
        else:
            print(ans[0],ans[1])
                 
