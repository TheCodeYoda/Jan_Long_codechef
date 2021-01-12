import sys
t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if(n==1):
        print(-1)
    else:
        dp=[[sys.maxsize for i in range(k+1)] for j in range(n+1)]
        a.sort()
        suffix_sum=[0 for i in range(n)]
        suffix_sum[n-1]=a[n-1]
        for i in range(n-2,-1,-1):
            suffix_sum[i]=suffix_sum[i+1]+a[i]
        for i in range(n-1,-1,-1):
            for j in range(k,-1,-1):
                if(j<=a[i]):
                    dp[i][j]=a[i]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j-a[i]]+a[i])
        flag=0
        for i in range(n-1,-1,-1):
            if(suffix_sum[i]-dp[i][k]>=k):
                flag=1
                print(n-i)
                break
        if(flag==0):
            print(-1)
        
