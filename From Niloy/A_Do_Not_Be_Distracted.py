t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    seen = set()
    suspicious = False
    last_char =''

    for ch in s:
        if ch != last_char:
            if ch in seen:
                suspicious = True
                break
            seen.add(ch)
            last_char = ch

    print("NO" if suspicious else "YES")
