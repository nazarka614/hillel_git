num = int(input("Введите число: "))

if num < 0:
    print("Факториал отрицательного числа не определен.")
elif num == 0:
    print("Факториал 0 равен 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Факториал {num} равен {factorial}")
