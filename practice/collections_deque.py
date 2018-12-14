from collections import deque

d = deque()

for _ in range(int(input())):
  func = input().split()
  getattr(d, func[0])(*[int(func[1])] if len(func) > 1 else [])

print(*d)