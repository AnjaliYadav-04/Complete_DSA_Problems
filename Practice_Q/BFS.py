from collections import deque

start = input().strip()
end = input().strip()

n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())

queue = deque([(start, 1)])

while queue:
    word, steps = queue.popleft()

    if word == end:
        print(steps)
        exit()

    for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + c + word[i+1:]

            if new_word in words:
                queue.append((new_word, steps + 1))
                words.remove(new_word)

print(-1)
