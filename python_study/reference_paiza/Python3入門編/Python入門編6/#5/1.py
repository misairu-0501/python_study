#リストの中身をループで表示する

enemies = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"]
# ここに、要素をループで表示するコードを記述する
for (i, enemy) in enumerate(enemies, 1):
    print(str(i) + "番目の" + enemy +"が現れた")
