#課題1

# a = 11
# b = 3

# print("11 + 3 =",a+b)
# print("11 - 3 =",a-b)
# print("11 × 3 =",a*b)
# print("11 ÷ 3 =",a//b,"余り",a%b)


#課題2
# print("1つ目の値を入力してください")
# num1 = int(input())
# print("2つ目の値を入力してください")
# num2 = int(input())

# print("合計：",num1+num2)
# print("平均：",(num1+num2)/2)


#課題3
# print("体重を入力してください")
# weight = int(input())
# print("身長を入力してください")
# height = int(input())

# BMI = weight//height*height
# print(BMI)

# if BMI < 18.5:
#     print("あなたは「やせ」です。")
# elif 18.5 <= BMI < 25:
#     print("あなたは「標準」です。")
# elif 25 <= BMI <30:
#     print("あなたは「肥満」です。")
# else:
#     print("あなたは「高度肥満」です。")


#課題4
a = 250000
b = 1+0.14/12
c = 30000

print(a*b-c)

for a in range(9):
    a = (a*b-c)
    print(a)