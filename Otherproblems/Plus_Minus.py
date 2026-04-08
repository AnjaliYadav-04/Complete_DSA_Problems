#!/bin/python3

def plusMinus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)
