# 標準入力から、2次元リストを読み込む

# 標準入力のデータ
# 0,0,1,1,0,0
# 0,1,0,0,1,0
# 1,0,0,0,0,1
# 1,1,1,1,1,1
# 1,0,0,0,0,1
# 1,0,0,0,0,1
# _

letter_A = []
while True:
    line = input()
    if line == "_":
        break
    # ここに、読み込んだデータをリストに追加するコードを記述する
    letter_A.append(line.split(","))
print(letter_A)
