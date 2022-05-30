# coding: utf-8
# 特定期間の西暦年と昭和年の対応表を作る
# 1行目：開始年
# 2行目：期間
# 昭和年 = 西暦年 - 1925
# 出力：西暦XXXX年は昭和YY年です
year = int(input())
term = int(input())

for i in range(term):
    seireki = year + i
    print("西暦" + str(seireki) + "年は", end = "")
    shouwa = seireki - 1925
    print("昭和" + str(shouwa) + "年です")
