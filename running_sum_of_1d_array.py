def running_sum(nums):
    if not nums:
        return
    
    cum_sum = 0 # cummulative_sum
    for i in range(len(nums)):
        cum_sum += nums[i]
        nums[i] = cum_sum

    return nums

nums = [1,2,3,4]
print(running_sum(nums))