# python用のパッケージを読み込む
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# カメラの設定値を決めておく
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# 繰り返し: 無限ループ
while True:

	# 繰り返し: 無限ループ
	while True:
		# 例外処理-プランA: 下の処理を実行（色相値の入力を受付ける）
		try:
			hue_value = int(input("10 から 245 までの色相値を指定してください: "))
			# 条件分岐: 10 から 245 以外の数値が入力された場合、プランBに移行するための処理を実行
			if (hue_value < 10) or (hue_value > 245):
				raise ValueError

		# 例外処理-プランB: 上の処理が失敗した場合の処理
		except ValueError:
			print("10 から245 ではない数値が入力されました！ もう一度入力してください。")

		# 例外処理-プランC: プランAもBも失敗した場合の処理
		else:
			break	# ループを抜ける

	lower_red = np.array([hue_value-10,100,100])
	upper_red = np.array([hue_value+10, 255, 255])

	# 繰り返し: カメラ映像、HSV、カラーマスク、最終結果の映像出力を4つのウィンドウにそれぞれ表示する
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		color_mask = cv2.inRange(hsv, lower_red, upper_red)

		result = cv2.bitwise_and(image, image, mask= color_mask)

		cv2.imshow("カメラ映像: ", image)
		cv2.imshow("HSV: ", hsv)
		cv2.imshow("Color Mask: ", color_mask)
		cv2.imshow("Final Result: ", result)

		rawCapture.truncate(0)

		k = cv2.waitKey(5) #& 0xFF

		# 条件分岐: いずれかの映像選択時にqが入力されたとき
		if "q" == chr(k & 255):
			break	# ループを抜ける

