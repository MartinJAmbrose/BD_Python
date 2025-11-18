# Find. In this case the largest number in a list.
def find_max(nums):
    max_so_far = float("-inf")
    if not nums:
        return float("-inf")
    max_so_far = float("-inf")
    for n in nums:
        if n > max_so_far:
            max_so_far = n
    return max_so_far