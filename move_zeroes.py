def move_zeroes(nums):
    
    c = 0
    for i in range(len(nums)):
        if i == len(nums) - 1:
            break

        if nums[i] == 0 and nums[i+1] != 0:
            c = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = c
        elif nums[i] == 0 and nums[i+1] == 0:
            continue

    print(nums)

nums = [0,1,0,3,12]
move_zeroes(nums)