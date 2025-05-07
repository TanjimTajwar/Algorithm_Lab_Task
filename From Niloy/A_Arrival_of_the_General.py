def min_swaps_to_form_line(n, heights):
    max_height = max(heights)
    min_height = min(heights)

    max_index = heights.index(max_height)  
    min_index = n - 1 - heights[::-1].index(min_height)  

    swaps = max_index + (n - 1 - min_index)
    if max_index > min_index:
        swaps -= 1  

    return swaps


n = int(input())
heights = list(map(int, input().split()))
print(min_swaps_to_form_line(n, heights))
