def birthdayCakeCandles(ar):
    maxx = max(ar)
    count = 0
    for i in ar:
        if i == maxx:
            count+= 1
    
    return count



ar = [3,2,1,3]
birthdayCakeCandles(ar)