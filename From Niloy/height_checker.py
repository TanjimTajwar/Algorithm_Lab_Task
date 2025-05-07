def height_check(height):
    expected=sorted(height)

    count=sum(height[i]!=expected[i] for i in range(len(height)))

    return count

n=int(input())

height=list(map(int,input().split()))

print(height_check(height))