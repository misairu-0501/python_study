# coding: utf-8
import random
omikuji = random.randint(1, 100)

if 30 <= omikuji <= 100:
	print("omikujiの中身は" + str(omikuji) + "なので大吉")
else:
	print("omikujiの中身は" + str(omikuji) + "なので大凶")
