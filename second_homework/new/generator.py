import numpy as np
import pandas as pd
import random as rnd
import string
import json
import pickle


def generate_name():
    name = ''
    name = name.join(rnd.choice(string.ascii_lowercase) for i in range(5))
    return name


def generate_parameters():
    mean = rnd.uniform(10, 20)
    std = rnd.uniform(5, 10)
    return mean, std


def generate_nums(mean, std, elements):
    num_list = list(np.random.normal(mean, std, elements))
    return num_list


def write_json(data, variant):
    file_name = 'var'+str(variant)+'.jsn'
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=10)


def write_csv(data, variant):
    file_name = 'var' + str(variant) + '.csv'
    frame = pd.DataFrame(data)
    frame.to_csv(file_name, index=False)


def write_pickle(data, variant):
    file_name = 'var' + str(variant) + '.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)


def create_variant(variant, columns, elements):
    data = {}
    info = {}
    for i in range(columns):
        column_name = generate_name()
        parameters = generate_parameters()
        num_list = generate_nums(parameters[0], parameters[1], elements)
        data[column_name] = num_list
        info[column_name] = parameters
    exp = rnd.choice(['jsn', 'csv', 'pkl'])
    if exp == 'jsn':
        write_json(data, variant)
    elif exp == 'csv':
        write_csv(data, variant)
    else:
        write_pickle(data, variant)
    return info


def create_files(variants, columns, elements):
    info = {}
    for i in range(variants):
        var_inf = create_variant(i, columns, elements)
        info[i] = var_inf
    with open('information.jsn', 'w') as file:
        json.dump(info, file, indent=10)


number_of_variants = int(input('Количество вариантов: '))
number_of_columns = int(input('Количество столбцов: '))
number_of_elements = int(input('Количество элементов: '))

create_files(number_of_variants, number_of_columns, number_of_elements)


