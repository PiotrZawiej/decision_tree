from file_atributes import convert_to_columns, quantity_of_attributes, all_variants_of_attributes
from Entropy import entropy_function, info_function
from gain_functions import gain_ratio_function


def wybor_najlepszego_podzialu(dane):
    global columns, decision_atribute_index, decision_atribute_entropy
    columns = dane 
    decision_atribute_index = len(columns) - 1
    decision_atribute_entropy = entropy_function(quantity_of_attributes(columns, all_variants_of_attributes(columns))[decision_atribute_index])

    gain_ratios = gain_ratio_function()
    najlepszy_atrybut = max(gain_ratios, key=gain_ratios.get)
    return najlepszy_atrybut


def decison_class(dane):
    decision_column = dane[-1]
    return all(val == decision_column[0] for val in decision_column)


def klasa_decyzyjna(dane):
    decision_column = dane[-1]
    frequency = {}

    for val in decision_column:
        if val in frequency:
            frequency[val] += 1
        else:
            frequency[val] = 1

    max_count = -1
    most_common = None
    for val, count in frequency.items():
        if count > max_count:
            max_count = count
            most_common = val

    return most_common


def data_descendant_for_value(dane, test_index, wartosc_index):
    attribute_column = dane[test_index - 1] 
    unique_values = list(set(attribute_column))
    target_value = unique_values[wartosc_index]

    filtered_rows = [
        [col[i] for col in dane]
        for i in range(len(attribute_column))
        if attribute_column[i] == target_value
    ]

    return list(map(list, zip(*filtered_rows)))


class Wezel:
    def __init__(self):
        self.test = None
        self.potomkowie = []
        self.klasa_dec = None


def tree_contructo(dane):
    w = Wezel()
    if not decison_class(dane):
        w.test = wybor_najlepszego_podzialu(dane)
        unique_values = list(set(dane[w.test - 1]))  
        for i in range(len(unique_values)):
            dane_potomka = data_descendant_for_value(dane, w.test, i)
            w.potomkowie.append(tree_contructo(dane_potomka))
            print(i)

    else:
        w.klasa_dec = klasa_decyzyjna(dane)
    return w

columns = convert_to_columns(r"test\test2.txt")
print(tree_contructo(columns))
