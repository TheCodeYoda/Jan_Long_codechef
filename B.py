t=int(input())

def trim(i,s,l,r):
    #print(i,l,r)
    if(i==4 or l==r):
        return r
    if(s[i]=='1'):
        l=(l+r)//2
    elif(s[i]=='0'):
        r=(l+r)//2
    return trim(i+1,s,l,r)

for _ in range(t):
    n=int(input())
    s=input()
    a=[chr(i) for i in range(97,97+16)]
    #print(a)
    ans=""
    for i in range(0,n,4):
        encoded=s[i:i+4]
        #print(encoded)
        index=trim(0,encoded,0,15)
        #print(index,i+index)
        ans+=a[index]
    print(ans)
        
