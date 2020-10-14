quizlist = [
	["42tokyoのクラスターはどこ？", "秋葉原", "パリ", "六本木", 3], 
	["今日の天気は？", "曇り", "晴れ", "雨", 2], 
	["次のうちTIGなのはどれ？", "クラスターで水を飲む", "クラスターで机上に水筒を置く", "クラスターでスタッフと話す", 2], 
	["クラスター付近が撮影場所だったドラマは？", "半沢直樹", "白い巨塔", "SUITS", 1] 
]

import random
random.shuffle(quizlist)

for quiz in quizlist:
	print("[問題]")
	print(quiz[0])
	for i in range(3):
		no = i + 1
		print(str(no) + ": " + quiz[no])
	user = int(input("答えは？"))
	ans = quiz[4]
	if user == ans:
		print("せいかーい！")
	else:
		print("残念でした。。。　答えは。。。" + quiz[ans])
	print(" ---- ")
