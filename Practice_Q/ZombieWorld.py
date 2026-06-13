n = int(input())
total_attacks = 0

for _ in range(n):
    health, power = map(int, input().split())
    
    attacks = 0
    while health > 0:
        health -= power
        attacks += 1
        if health > 0:
            health *= 2
    
    total_attacks += attacks

print(total_attacks)
