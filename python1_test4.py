# 借入金額
debt = 250000
# 年利/12(月利)
interest = 1 + 0.14 / 12
# 月々の返済金額
repay = 30000
# 返済期間（月ごと）
month = 0

while debt > 0:
    debt = debt * interest
    month += 1
    if debt > repay:
        debt -= repay
        print(month,"ヶ月目:返済額=",repay,"円,","残り",debt)
    else:
        print(month,"ヶ月目:返済額=",debt,"円,","返済完了")
        break