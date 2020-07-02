# 速度と距離から時間を計算
def time(speed,distance):
    time = distance / speed
    return time

# 速度と距離を取得
print("速度を入力してください")
speed = int(input())
print("距離を入力してください")
distance = int(input())

# 時間を出力
print("時間は",time(speed,distance))
