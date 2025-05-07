def check_word_length(word):
    if len(word) > 10:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
    else:
        print(word)

# Example usage

t=int(input())

for _ in range(t):
    word = input()
    check_word_length(word)