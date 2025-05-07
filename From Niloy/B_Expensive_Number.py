from itertools import combinations

def minimum_koita_shorano_jai(num_str):
    best_cost = float('inf')
    min_removed_digits = len(num_str)

    digits = list(num_str)
    total_len = len(digits)

    for subseq_len in range(1, min(15, total_len) + 1):
        for idx_group in combinations(range(total_len), subseq_len):
            subseq = [digits[i] for i in idx_group]
            subseq_str = ''.join(subseq)
            value = int(subseq_str)
            digit_sum = sum(int(d) for d in subseq_str)
            if digit_sum == 0:
                continue
            cost = value / digit_sum
            removed = total_len - subseq_len
            if cost < best_cost or (abs(cost - best_cost) < 1e-9 and removed < min_removed_digits):
                best_cost = cost
                min_removed_digits = removed

    return min_removed_digits

t = int(input())
for _ in range(t):
    number = input().strip()
    print(minimum_koita_shorano_jai(number))
