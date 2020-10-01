"""Каждый день я пробегаю «следующую степень двойки» км. Сколько дней пройдет, пока
я в сумме пробегу 1000 км? 10000 км?"""
print("Задание 1.1")


def s1t1(n):
    day = 0
    km = 0
    while km < n:
        km += 2**day
        day += 1
    return day


print("1000 километров за ", s1t1(1000), "дней")
print("10000 километров за ", s1t1(10000), "дней")

"""Начав тренировки, спортсмен в первый день пробежал 10 км. Для увеличения
выносливости ему необходимо повышать норму бега через одну тренировку на 15% от
нормы предыдущей тренировки. Спортсмен тренируется каждый день. Какой
суммарный путь он пробежит за 30 дней."""
print("Задание 1.3")


def s1t3(days):
    km = 10
    sum = 0
    day = 1
    while day <= days:
        if day % 2 == 0:
            km *= 1.15
        sum += km
        day += 1
    return sum


print(s1t3(30), "км за 30 дней")


"""Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый следующий день
он увеличивал дневную норму на 10% от нормы предыдущего дня. Через сколько дней:
а) спортсмен будет пробегать в день больше 20 км;
b) пробежит суммарный путь 100 км."""

print("Задание 1.4")


def s1t4():
    res = [0, 0]
    km = 10
    day = 1
    sum = 0
    while True:
        sum += km
        if km > 20 and res[0] == 0:
            res[0] = day
        if sum >= 100 and res[1] == 0:
            res[1] = day
        if res[0] > 0 and res[1] > 0:
            break
        km *= 1.1
        day += 1
    return res


print(s1t4())


# Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...


print("Задание 2.1")


def s2t1(n):
    first_val = 1
    second_val = 1
    l = [first_val,second_val]
    for _ in range(1,15):
        sum = first_val+second_val
        l.append(sum)
        first_val=second_val
        second_val=sum
    return l[n-1]


print("Девятый член последовательности =", s2t1(9))


# Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…


print("Задание 2.2")


def s2t2(n):
    first_val = 1
    second_val = 1
    third_val = 1
    l = [first_val, second_val, third_val]
    for _ in range(1,15):
        sum = first_val+second_val+third_val
        l.append(sum)
        first_val = second_val
        second_val = third_val
        third_val = sum
    return l[n-1]


print("Девятый член последовательности =", s2t2(9))


# Вывести квадраты нечетных чисел до N. (генератором списков)


print("Задание 2.3")


def s2t3(n):
    l = [i**2 for i in range(1, n + 1, 2)]
    return l


print(s2t3(17))


# Вычислить сумму и произведение всех натуральных чисел от А до В включительно.


print("Задание 2.4")


def s2t4(a,b):
    l = [i for i in range(a, b+1)]
    sum = 0
    prod = 1
    for i in l:
        sum += i
        prod *= i
    return sum, prod


print(s2t4(1, 7))


"""Даны натуральные числа А и В.
Вывести сначала все чётные числа, заключённые между ними, потом все нечётные (генератором/ами списков)"""


print("Задание 3.5")


def s2t5(a, b):
    if a % 2 == 0:
        even = [i for i in range(a, b+1, 2)]
        odd = [i for i in range(a+1, b, 2)]
    else:
        even = [i for i in range(a+1, b, 2)]
        odd = [i for i in range(a, b+1, 2)]
    return even, odd


print(s2t5(3, 14))


"""Исходный список содержит положительные и отрицательные числа.
Требуется положительные поместить в один список, а отрицательные - в другой (генератором/ами списков)"""


print("Задание 2.5")


def s2t5():
    l = [11, 5, -9, 6, -13, -5, 71, 23, -4]
    positive = [i for i in l if i>0]
    negative = [i for i in l if i<0]
    return positive, negative


print(s2t5())


# Нарисовать рамочку шириной w символов и высотой h символов


print("Задание 3.1")


def s3t1(w, h):
    print(w * "*")
    for i in range(2, h):
        print("*" + (w - 2) * " " + "*")
    print(w * "*")


s3t1(5, 3)


# Пускай символ, которым рисуется рамочка – тоже входной параметр.


print("Задание 3.2")


def s3t2(w, h, s):
    print(w * s)
    for i in range(2, h):
        print(s + (w - 2) * " " + s)
    print(w * s)


s3t2(7, 6, "@")


# Нарисовать рамочку шириной w символов и высотой h символов, и толщиной f символов. (оформить в виде функции)


print("Задание 3.3")


def s3t3(w, h, f, s):
    for i in range(f):
        print(w * s)
    for i in range(0, h - f * 2):
        print(f * s + (w - 2 * f) * " " + f * s)
    for i in range(0, f):
        print(w * s)


s3t3(10, 7, 2, "~")