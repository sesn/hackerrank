from collections import OrderedDict

wordDict = OrderedDict()

for _ in range(int(input())):
  word = input()
  wordDict[word] = wordDict.get(word, 0) + 1

print(len(wordDict))
print(*[n for word, n in wordDict.items()])