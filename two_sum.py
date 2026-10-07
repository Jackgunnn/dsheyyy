def two_sum(arr, target):
    seen = {}
    for i in range(len(arr)):
        diff = target - arr[i]
       
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[arr[i]] = i
                

arr = [2,5,7,9]
target = 9
t = two_sum(arr, target)
print(t)