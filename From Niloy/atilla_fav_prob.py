def find_ans():
    line_size = int(input())

    line = input()

    max_char = 'a'

    for ch in line:
      if ch>max_char:
        max_char = ch
    
    return ord(max_char) - ord('a') +1

def test_case(t):
   for _ in range(t):
      result = find_ans()
      print(result)

if __name__ == "__main__":
   t = int(input())

   test_case(t)