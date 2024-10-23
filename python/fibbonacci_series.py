N=int(input())
a=0
b=1
if N==1:
    print(a)
elif N==2:
    print(a,b)
elif N>2:
    print(a,b,end=' ')
    for i in range(3,N+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c