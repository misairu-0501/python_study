def add5(x):
  return x + 5

list1 = [4, 2, 5, 8, 9, 1]
map_object = map(add5, list1)

for i in map_object:
  print(i)