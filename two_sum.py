def two_sum(arr, target):
    for num in arr:
        diff = target - num
        if diff in arr and diff != num:
            return num, diff

arr = [3,2,4]
target = 6
t = two_sum(arr, target)
print(t)