def move_zeroes(nums):
    i = 0 
    c = 0
    while True:
        if i == len(nums) - 2:
            break
    
        elif nums[i] == 0 and nums[i+1] != 0:
            c = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = c
           
            # print(i, nums)

        elif nums[i] == 0 and nums[i+1] == 0:
            c = nums[i]
            nums[i] = nums[i+2]
            nums[i+2] = c
         
            # print(i, nums)
        
        i+=1
            

        

    print(nums)

nums = [0,1,0,3,12]
move_zeroes(nums)