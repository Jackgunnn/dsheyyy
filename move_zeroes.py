#IN-PLACE OPERATIONS within same list using nested for loops
def move_zeroes(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
               
    return nums

nums_list = [[0,1,0,3,12],
             [0,0,1],
             [1,2,3],
             [0,0,0],
             [4,0,5,0,3]]

for nums in nums_list:    
    print(move_zeroes(nums))