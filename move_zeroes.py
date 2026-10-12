def move_zeroes(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0

            elif nums[i] == 0 and nums[j] == 0:
                j = j+1
                nums[i] = nums[j]
                nums[j] = 0            

        

    print(nums)

nums = [0,1,0,3,12]
move_zeroes(nums)