# 閏年かどうか判定
def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 現在日時を取得
import datetime
now = datetime.datetime.now()

# 今年は閏年かどうか
if isleap(now.year):
    print("今年は閏年です。")
else:
    print("今年は閏年ではないです。")

# 昨年は閏年かどうか
if isleap(now.year - 1):
    print("昨年は閏年です。")
else:
    print("昨年は閏年ではないです。")

# 来年は閏年かどうか
if isleap(now.year + 1):
    print("来年は閏年です。")
else:
    print("来年は閏年ではないです。")