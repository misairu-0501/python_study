list1 = ['a', 'b', 'c', 'd']
list2 = ['A', 'B', 'C']

for (item1, item2) in zip(list1, list2):
  print('{} : {}'.format(item1, item2))