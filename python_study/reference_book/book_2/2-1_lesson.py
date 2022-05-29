st = 1950
ed = 2050

print('うるう年一覧')
for i in range(st, ed + 1):
  if (i % 4 == 0) and (not (i % 100 ==  0 and  i % 400 != 0)):
    print(i)

