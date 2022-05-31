# ループで辞書のキーと値を出力しよう

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、ハッシュの値をループで出力してみよう
for (key, value) in skills.items():
    print(key + "は" + str(value) + "です")