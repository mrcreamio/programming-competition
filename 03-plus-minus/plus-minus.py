def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(str.format('{0:.6f}', (positive/len(arr))))
    print(str.format('{0:.6f}', (negative/len(arr))))
    print(str.format('{0:.6f}', (zero/len(arr))))
    
arrr = [-4,3,-9,0,4,1]
plusMinus(arrr)
