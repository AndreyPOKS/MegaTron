# программа калькулятор
# num1 = int(input("Введи первое число:   "))
# num2 = int(input("Введи второе число:   "))
# calc = input("Введи знак операции:  ")
#
# if calc == '+':
#     print(num1 + num2)
# elif calc == '*':
#     print(num1 * num2)
# elif calc == '-':
#     print(num1 - num2)
# elif calc == '/':
#     print(num1 / num2)

# 23.5897

# Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
# (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно»,
# 4 — «хорошо», 5 — «отлично»). Если K не лежит в диапазоне 1-5, то вывести строку «ошибка».

# k = int(input("Введи число:   "))
#
# if k == 1:
#     print("Плохо")
# elif k == 2:
#     print("Неудовлетворительно")
# elif k == 3:
#     print("Удовлетворительно")
# elif k == 4:
#     print("Хорошо")
# elif k == 5:
#     print("Отлично")
# else:
#     print("Нет такой оценки!!!!!!")

#PEP8
#< > => !=



# Размер скидки на продукты определен следующим образом:
# при покупке до 500 р. скидка составит 2%;
# при покупке от 500 р. до 1000 р. скидка составит 3%;
# при покупке от 1000 р. до 1500 р. скидка составит 4%;
# при покупке от 1500 р. до 2000 р. скидка составит 5%.
# Составить программу определяющую размер скидки в зависимости от
# потраченной суммы.

s = int(input("Введите стоимость покупки: "))

if s < 500:
    print("Размер скидки 2%");
elif 500 <= s < 1000:
    print("Размер скидки 3%");

