# datetimeインポート
import datetime

# 閏年を判定する関数
def isleap(year,year_name):
    if year % 100 == 0 and year % 400 != 0:
        print("{}は閏年ではありません".format(year_name))
    elif year % 4 == 0:
        print("{}は閏年です".format(year_name))
    else:
        print("{}は閏年ではありません".format(year_name))

# 昨年から来年までのリスト
year_list = ["昨年","今年","来年"]

# 現在日時を取得
now = datetime.datetime.now()

# 昨年から来年までの閏年を判定
for i,year_name in enumerate(year_list):
    year = now.year - 1 + i
    isleap(year,year_name)