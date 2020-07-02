print("体重を入力してください(kg)")
weight = int(input())
print("身長を入力してください(cm)")
height = int(input())

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    print("あなたは「やせ」です。")
elif 18.5 <= bmi < 25:
    print("あなたは「標準」です。")
elif 25 <= bmi < 30:
    print("あなたは「肥満」です。")
else:
    print("あなたは「高度肥満」です。")
