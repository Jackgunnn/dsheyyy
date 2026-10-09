def contains_duplicate(nums):
    seen = {}
    for i in nums:
        if i not in seen:
            seen[i] = 1
        else:
            return True
    return False


nums = [1,2,3]
print(contains_duplicate(nums)) 