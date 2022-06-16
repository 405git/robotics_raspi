# python用のパッケージを読み込む
import gpiozero
import time

"""
=====================================
   !!! コードは一部未完成です。!!!

 これまでのソースコードをよく読んで
 このコードを完成させよう。

 ソースコードの読み方:
     $ cat ファイル名.拡張子

 例:
     $ cat 01_move_test.py
=====================================
"""

# 変数「TRIG」と「ECHO」は未完成です！
TRIG = 
ECHO = 

# 変数「trigger」,「echo」は未完成です！
trigger = gpiozero.OutputDevice()
echo = gpiozero.DigitalInputDevice()

# 変数「robot」は未完成です！
robot = gpiozero.Robot()


# 障害物までの距離を計測するための処理を関数「get_distance」として定義しておく
# （関数化することでコードをひとまとめにしておいて、あとで何度も呼び出せる様にしておく）
def get_distance(trigger, echo):
	trigger.on()
	time.sleep(0.00001)
	trigger.off()

	while echo.is_active == False:
		pulse_start = time.time()

	while echo.is_active == True:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = 34300 * (pulse_duration/2)

	round_distance = round(distance,1)

	return(round_distance)


# 繰り返し:以下のコードを無限ループさせる
while True:
	print("障害物回避プログラムを開始します。\n終了する場合は ctrl + c を押してください。")
	# 関数「get_distance」を使って障害物までの距離を計測し、変数「dist」に代入
	dist = get_distance(trigger,echo)

	# 条件分岐: 変数「dist」の値を見て 15 以下の場合、続く処理を実行
	if dist <= 15:
		print("前方に障害物を検出しました。 右に回転します。")
		# ロボットを右に0.3秒回転させる
		robot.right(0.3)
		# 0.25秒間待機
		time.sleep(0.25)

	# 条件分岐: 変数「dist」の値を見て 15 以下でない場合、続く処理を実行
	else:
		print("安全を確認しました。 前進します。")
		# ロボットを0.3秒前進させる
		robot.forward(0.3)
		# 0.1秒間待機
		time.sleep(0.1)
