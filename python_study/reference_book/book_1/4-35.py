taro = ('taro', 180, 80)
jiro = ('jiro', 170, 70)
saburo =('saburo', 160, 60)
list1 = [taro, jiro, saburo]

sum_height = 0
for (name, height, weight) in list1:
  sum_height += height

print(sum_height/len(list1))



