# python用のライブラリを読み込む
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero

# カメラの設定値を決めておく
camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(image_width, image_height))
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000

# モータの設定値を決めておく
robot = gpiozero.Robot(left=(17,18), right=(27,22))
forward_speed = 0.3
turn_speed = 0.25

# 検出したい色相値を指定する
HUE_VAL = 28

lower_color = np.array([HUE_VAL-10,100,100])
upper_color = np.array([HUE_VAL+10, 255, 255])


# 繰り返し: カメラフレームを解析する
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	color_mask = cv2.inRange(hsv, lower_color, upper_color)

	contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	object_area = 0
	object_x = 0
	object_y = 0

	# 繰り返し: 輪郭の大きさにより目標物体を特定する
	for contour in contours:
		x, y, width, height = cv2.boundingRect(contour)
		found_area = width * height
		center_x = x + (width / 2)
		center_y = y + (height / 2)

		# 条件分岐: 検出された物体の中で最も大きい領域の面積と中心座標に変数の値を更新する
		if object_area < found_area:
			object_area = found_area
			object_x = center_x
			object_y = center_y

	# 条件分岐: 目標物体の最終的な面積が0より大きいか調査
	if object_area > 0:
		ball_location = [object_area, object_x, object_y]

	# 条件分岐: 目標物体の最終的な面積が0より大きくない場合
	else:
		ball_location = None


	# 条件分岐: ロボットを目標物体に反応させる
	if ball_location:

		# 条件分岐: 
		if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):

			# 条件分岐: 
			if ball_location[1] > (center_image_x + (image_width/3)):
				robot.right(turn_speed)
				print("右へ回転")

			# 条件分岐: 
			elif ball_location[1] < (center_image_x - (image_width/3)):
				robot.left(turn_speed)
				print("左へ回転")

			# 条件分岐: 
			else:
				robot.forward(forward_speed)
				print("前進")

		# 条件分岐: 
		elif (ball_location[0] < minimum_area):
			robot.left(turn_speed)
			print("ターゲットとの距離が遠すぎるようです。サーチします。")
		# 条件分岐: 
		else:
			robot.stop()
			print("ターゲットへの接近が完了しました。停止します。")
	# 条件分岐: 
	else:
		robot.left(turn_speed)
		print("ターゲットが見つかりません。サーチします。")

	rawCapture.truncate(0)
