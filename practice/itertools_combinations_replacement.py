from itertools import combinations_with_replacement as combs

s, k = input().split()
print(*[''.join(p) for p in combs(sorted(s), int(k))], sep='\n')