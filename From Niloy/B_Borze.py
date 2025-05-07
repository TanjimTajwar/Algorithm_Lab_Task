code = input()
i = 0
result = ""

while i < len(code):
    if code[i] == '.':
        result += '0'
        i += 1
    elif code[i] == '-':
        if code[i + 1] == '.':
            result += '1'
        else:  # code[i + 1] == '-'
            result += '2'
        i += 2

print(result)
