# get Set A elemets
set_A = set(map(int, input().split()))

# get numbers of subset to check strict sets functionality
num_test_sets = int(input())

result = True
for i in range(num_test_sets):
  sub_set = set(map(int, input().split()))
  if len(set_A.difference(sub_set)) > 0 and len(sub_set.difference(set_A)) == 0:
    result = result and True
  else:
    result = False

print(result)