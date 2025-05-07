k=int(input())

a=list(map(int,input().split()))

cumulative=0
months=0
a.sort(reverse=True)


if k==0:
    print(0)

else:
    for i in a:
        cumulative+=i
        months+=1
        if cumulative>=k:
            print(months)
            break
    else:
        print(-1)
