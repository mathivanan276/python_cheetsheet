"""Given a list of integers, return the two numbers that add up to a target sum."

 This checks if the candidate can:
1. Traverse a list
2. Use nested loops or hashing
3. Return correct pair
"""

nums = [2, 7, 11, 15]
target = 9
# Expected Output: (2, 7)

nums_2 = [1, 2, 3, 4, 5, 6, 7]
target_2 = 8

nums_3 = [2, 2, 3, 3, 4, 4]
target_3 = 6

nums_4 = list(range(1, 10_000_001))  # [1, 2, 3, ..., 10 million]
target_4 = 19_999_999

def find_target_sum(nums: list, target: int) -> list:
    """Returns set of numbers available in list that addes up to given target."""
    
    pairs = set()
    
    left, right = 0, 0
    
    while left < len(nums) -1:
        right = len(nums) - left - 1
        while right > left:
            if target == nums[left] + nums[right]:
                pairs.add(tuple(sorted((nums[left], nums[right]))))
            right -= 1
        left += 1
    
    return pairs

def find_target_sum_sorted(nums: list, target: int) -> set:
    pairs = set()
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            pairs.add((nums[left], nums[right]))
            left_val, right_val = nums[left], nums[right]
            # Skip duplicates
            while left < right and nums[left] == left_val:
                left += 1
            while left < right and nums[right] == right_val:
                right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return pairs

def find_target_sum_sorted_gen(nums: list, target: int):
    """
    Generator version of two-pointer sum finder.
    Yields pairs instead of storing them in memory.
    Works best if nums is sorted.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            yield (nums[left], nums[right])   # yield instead of storing
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

print(find_target_sum(nums, target))
print(find_target_sum(nums_2, target_2))
print(find_target_sum(nums_3, target_3))
# print(find_target_sum_sorted(nums_4, target_4))
pairs = find_target_sum_sorted_gen(nums_4, target_4)
print(next(pairs))