# coding: utf-8
import random
age = random.randint(18, 22)    # ageに、何才かを18~22の範囲でランダムに代入
text = ""
if age < 20:
    text = "飲酒禁止"
else:
    text = "飲酒可能"
print(str(age) + "才は" + text)
