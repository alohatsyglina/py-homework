"""Создайте программу для перевода из одной системы мер в другую
(Цельсий - Фаренгейт, мили - километры, унции - граммы и т.д.). """


def lbs_to_kg(value):
    res = round(value*0.453, 1)
    print(value, 'lbs is', res, ' kg')


def oz_to_grams(value):
    res = round(value*28.35, 1)
    print(value, 'oz is ', res, 'g')


def celsius_to_fahrenheit(value):
    res = round(value*(9/5)+32, 1)
    print(value, '°C is ', res, '°F')


def celsius_to_kelvin(value):
    res = value + 273
    print(value, '°C is', res, 'K')


def meters_to_yards(value):
    res = round(value*1.09, 1)
    print(value, 'm is', res, 'yd')


def km_to_miles(value):
    res = round(value*0.62, 1)
    print(value, 'km is', res, 'mi')


def centimeters_to_inches(value):
    res = round(value*0.393, 1)
    print(value, 'cm is', res, 'in')


def converter(i, value):
    dict = {1: lbs_to_kg, 2: oz_to_grams, 3: celsius_to_fahrenheit, 4: celsius_to_kelvin, 5: meters_to_yards,
            6: km_to_miles, 7: centimeters_to_inches}
    return dict[i](value)


choice = int(input('press 1 to convert lbs to kilograms\n'
                   'press 2 to convert ounces to grams\n'
                   'press 3 to convert Celsius to Fahrenheit\n'
                   'press 4 to convert Celsius to Kelvin\n'
                   'press 5 to convert meters to yards\n'
                   'press 6 to convert kilometers to miles\n'
                   'press 7 to convert centimeters to inches\n'))
value = int(input('enter the value to convert\n'))
try:
    converter(choice, value)
except KeyError:
    print('please enter a number from 1 to 7 before entering the value to convert')




