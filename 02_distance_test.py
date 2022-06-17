# python用のパッケージを読み込む
import gpiozero
import time

# 変数「TRIG」に数値の23を割り当てる（代入）
TRIG = 23
# 変数「ECHO」に数値の24を割り当てる（代入）
ECHO = 24

# 変数「trigger」にラズパイのGPIOピンの変数「TRIG」番を割り当てる（代入）
trigger = gpiozero.OutputDevice(TRIG)
# 変数「echo」にラズパイのGPIOピンの変数「ECHO」番を割り当てる（代入）
echo = gpiozero.DigitalInputDevice(ECHO)

'''
 Tips:
	trigger（トリガー）は超音波センサからpingと呼ばれる信号を発射する側、
	echo（エコー）は物体に当たって跳ね返ってきた信号を受信する側　としての役割がある
'''

# トリガーを一時的にONにして超音波センサから信号を発射し、すぐにOFFにする
print("=========○ 信号発射 ○=========")
trigger.on()
time.sleep(0.00001)
trigger.off()


# 繰り返し: 変数「echo」のis_activeプロパティが「False」である間ずっと
while echo.is_active == False:
	# 変数「pulse_start」に現在時刻（Unix time形式）を代入
	pulse_start = time.time()
	# ※つまり、信号が発射された時の時刻を「pulse_start」に格納する
	print("信号を発射した時刻： " + str(pulse_start))

# 繰り返し: 変数「echo」のis_activeプロパティが「True」である間ずっと
while echo.is_active == True:
	# 変数「pulse_end」に現在時刻を代入
	pulse_end = time.time()
	# ※つまり、信号が物体に反射して返ってきた時の時刻(Unix time形式)を「pulse_end」に格納する
	print("反射した信号を受信した時刻: " + str(pulse_end))



# 変数「pulse_dulation」に変数「pulse_end」から変数「pulse_start」を引いた値を代入
#（つまり信号が行って帰ってくるまでの秒数を計算して「pulse_dulation」に代入している）
pulse_duration = pulse_end - pulse_start

# 変数「distance」に『音速(343m/s)の単位[cm/s]に変換 x 信号受信までの片道にかかった秒数』を計算して得られる『物体までの距離』を代入
distance = 34300 * (pulse_duration/2)

# 距離の値を小数点第1位に丸めて、変数「round_distance」に代入する
round_distance = round(distance,2)

print("距離: ", round_distance)
