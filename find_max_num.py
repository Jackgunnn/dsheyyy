def find_max(nums):
    if len(nums) == 0:
        print("Empty Array!")
        return
    
    maxxx = nums[0]
    for i in nums[1:]:
        if i > maxxx:
            maxxx=i

    return maxxx

nums = [-3,-1,-2,-6]
print(find_max(nums))



'''
NOTES:

for i in nums[1:]:

creates a new list containing all elements except the first. That uses O(n) additional space in Python.
If you want to keep the algorithm's auxiliary space at O(1), use an index-based loop:

for i in range(1, len(nums)):

Now you're not creating a sliced copy of the array.
'''