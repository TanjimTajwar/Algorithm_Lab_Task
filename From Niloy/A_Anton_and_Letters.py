s = input().strip()


s = s[1:-1]

if not s:
    print(0)
else:
    letters = s.split(", ")
    print(len(set(letters)))
