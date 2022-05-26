def is_even(x):
  return x % 2 == 0

list1 = [4, 2, 5, 8, 9, 1]
filter_object = filter(is_even, list1)

list2 = list(filter_object)
print(list2)
