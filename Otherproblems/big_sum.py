#!/bin/python3

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    print(aVeryBigSum(ar))
