def to_si(key, orig_value):
    to_si_rates = {1: 1, 2: 1000, 3: 0.01, 4: 0.001, 5: 1609.34, 6: 0.9144,
                   7: 0.3048, 8: 0.0254, 9: 1852}
    return to_si_rates[key] * orig_value


def from_si(key, value_in_si):
    from_si_rates = {1: 1, 2: 0.001, 3: 100, 4: 1000, 5: 0.000621371, 6: 1.09361,
                     7: 3.28048, 8: 39.3701, 9: 0.000539957}
    return round(from_si_rates[key] * value_in_si, 2)


names = {1: 'm', 2: 'km', 3: 'cm', 4: 'mm', 5: 'mi', 6: 'yd', 7: 'ft', 8: 'in', 9: 'nmi'}

print('Что переводим?\n1 - метры\n2 - километры\n3 - сантиметры\n4 - милиметры\n5 - мили\n'
      '6 - ярды\n7 - футы\n8 - дюймы\n9 - морские мили')
unit_from = int(input())
print('Во что переводим?\n1 - метры\n2 - километры\n3 - сантиметры\n4 - милиметры\n5 - мили\n'
      '6 - ярды\n7 - футы\n8 - дюймы\n9 - морские мили')
unit_to = int(input())
value = int(input('Значение для конвертации: '))

in_si = to_si(unit_from, value)
result = from_si(unit_to, in_si)
print(value, names[unit_from], ' = ', result, names[unit_to])

