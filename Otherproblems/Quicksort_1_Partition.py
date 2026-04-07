#!/bin/python3

def quickSort(arr):
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left + middle + right

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*quickSort(arr))
