# datetimeインポート
import datetime

# 閏年を判定する関数
def isleap(year,year_name):
    isleap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if year_name == 0:
        year_name = "今年"
    elif year_name == -1:
        year_name = "去年"
    else:
        year_name = "来年"
    if isleap:
        print("{}は閏年です。".format(year_name))
    else:
        print("{}は閏年ではありません。".format(year_name))

# 現在日時を取得
now = datetime.datetime.now()

# 昨年から来年までの閏年を判定
for year_name in range(-1,2):
    isleap(now.year + year_name,year_name)
