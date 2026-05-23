def pairs(arr, target):
    seen = {}
    for i,num in arr:
        diff = target - i
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return seen
arr=(2, 7, 11, 15) 
target = 9
print(pairs(arr, target))

            
