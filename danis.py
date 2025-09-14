#1
print("hello world")
#2
a=input("enter your name")
print("hello",a)
#3
num1=float(input("Введите 1 число"))
num2=float(input("Введите 2 число"))
sum=num1+num2
print("Сумма чисел:",sum)
#4
a1=float(input("Введите 1 число"))
b1=float(input("Введите 2 число"))
print("Сложение:",a1+b1)
print("Вычитание:",a1-b1)
print("Умножение:",a1*b1)
print("Деление:",a1/b1)
print("Целочисленное деление:",a1//b1)
print("Остаток от деление:",a1%b1)
print("Возведение в степень",a1**b1)

#5
a2 = int(input("Введите число: "))
if a2 % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")
#6
a3 = float(input("Введите число:"))
if a3 >0:
    print("Число положительное")
elif a3 < 0:
    print("Число отрицательное")
else:
    print("Число ноль")
#7
a4=int(input("Введите число"))
print("Таблица умножения для", a4)
for i in range(1,11):
    print(a4, "*", i, "=", a4*i)
#8
a5 = int(input("Введите число для вычисления факториала: "))
factorial = 1
for i in range(1, a5 + 1):
    factorial = factorial * i
print(factorial)
#9
a6 = int(input("Введите число: "))
if a6 < 2:
    print("Число не является простым")
else:
    for i in range(2, int(a6**0.5) + 1):
        if a6 % i == 0:
            print("Число не является простым")
            break
    else:
        print("Число простое")
#10
a7 = float(input("Введите первое число: "))
b7 = float(input("Введите второе число: "))
c7 = float(input("Введите третье число: "))
minimum = min(a7, b7, c7)
maximum = max(a7, b7, c7)
print("Наименьшее число:", maximum)
print("Наибольшее число:", minimum)


