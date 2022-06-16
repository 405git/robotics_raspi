# python用のパッケージを読み込む
import gpiozero
import time

# 変数「robot」にモータコントロール用のピンを割り当てる（代入）
robot = gpiozero.Robot(left=(17,18), right=(27,22))

# ユーザからの入力を受け付け、変数「get_key」に入力された値を割り当てる（代入）
get_key = input("モータの動作テストを開始します。\nタイヤを宙に浮かせたら、Enterを押してください。\n")

# 条件分岐: もしEnterが入力されたら
if (get_key == ""):

	print("モータの動作テストまで  ...3")
	print(" ... ")
	time.sleep(1)
	print("モータの動作テストまで  ...2")
	time.sleep(1)
	print(" .. ")
	print("モータの動作テストまで  ...1")
	time.sleep(1)
	print(".\n ------ 動作開始 ------ ")

	# 繰り返し: 以下の処理を4回繰り返す
	for i in range(4):
		robot.forward()	 # ロボットを前進させる
		time.sleep(0.5)  # 0.5秒間待機
		robot.right()    # ロボットを右に回転させる
		time.sleep(0.25) # 0.25秒間待機 
