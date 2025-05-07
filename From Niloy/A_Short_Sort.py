t = int(input())
valid = {"abc", "acb", "bac", "cba"}

for _ in range(t):
    s = input().strip()
    print("YES" if s in valid else "NO")
