import math
def miniMaxSum(arr):
    mini = 0
    maxi = 0
    arr = sorted(arr)
    for i in range(0,len(arr)-1):
        mini += arr[i]
    for i in range(1,len(arr)):
        maxi += arr[i]

    print(mini,maxi)



arr = [1,2,3,4,5]
miniMaxSum(arr)