Y, W = map(int, input().split())
M = max(Y, W)


prob = {
    1: "1/1",
    2: "5/6",
    3: "2/3",
    4: "1/2",
    5: "1/3",
    6: "1/6"
}

print(prob[M])
