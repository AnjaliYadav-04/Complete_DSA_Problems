#!/bin/python3

def bonAppetit(bill, k, b):
    total = (sum(bill) - bill[k]) // 2
    if total == b:
        print("Bon Appetit")
    else:
        print(b - total)

if __name__ == '__main__':
    n, k = map(int, input().split())
    bill = list(map(int, input().split()))
    b = int(input())
    bonAppetit(bill, k, b)
