import sys
from collections import defaultdict

n, m = map(int, input().split())
word_note = defaultdict(int)

for _ in range(n):
    word = sys.stdin.readline().strip()

    if len(word) >= m:
        word_note[word] += 1
            
new_word_note = sorted(word_note.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for word in new_word_note:
    print(word[0])
