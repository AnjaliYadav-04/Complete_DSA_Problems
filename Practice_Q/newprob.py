def plusMinus(arr):
    n = len(arr)
    pos = neg = zero = 0
    
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    
    print(pos / n)
    print(neg / n)
    print(zero / n)
