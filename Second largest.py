def second_largest(arr):
    n = len(arr)
    largest = max(arr)
    second = 0
    for i in range(n):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
            print(largest)
        else:
            second = arr[i]
    return second if second != largest else -1
arr = [10,10,10]
print(second_largest(arr)) 
