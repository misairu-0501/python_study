import sys

def era(year):
  if year >= 2019:
    print('令和' + str(year - 2018) + '年')
  elif year >= 1989:
    print('平成' + str(year - 1988) + '年')
  elif year >= 1926:
    print('昭和' + str(year - 1925) + '年')
  elif year >= 1912:
    print('大正' + str(year - 1911) + '年')
  elif year >= 1868:
    print('明治' + str(year - 1867) + '年')
  else:
    print('元号変換非対応です') 

year = input('西暦を入力して下さい:')

if not year.isdecimal():
  print('数字のみ入力して下さい')
  sys.exit()

year = int(year)

if not (1869 <= year <= 2020):
  print('元号変換非対応です')
  print('1969年以上2020年以下で入力して下さい')
  sys.exit()

era(year) 