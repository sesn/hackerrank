from collections import deque

ll = [];
for _ in range(int(input())):
  n = int(input())
  d = deque()
  d.extend(input().replace(' ',''))
  if n % 2 == 0:
    length = n/2 - 1
  else:
    length = n/2
  l = ''
  for i in range(int(length)):
    if d.pop() == d.popleft():
      l = 'Yes'
    else:
      l = 'No'
  ll.append(l)

print(*ll, sep="\n")
