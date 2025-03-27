import math
from file_atributes import convert_to_columns, quantity_of_attributes, all_variants_of_attributes

def entropy_function(count_atribute):

    total = sum(count_atribute.values())

    entropy = 0

    for count in count_atribute.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)

    return entropy


def info_function(attribute_column, decision_column):

    total_len = len(attribute_column)
    value_class_counts = {}

    # Grupowanie: dla każdej wartości atrybutu zliczamy klasy decyzyjne
    for attr_value, decision in zip(attribute_column, decision_column):
        if attr_value not in value_class_counts:
            value_class_counts[attr_value] = {}
        if decision not in value_class_counts[attr_value]:
            value_class_counts[attr_value][decision] = 0
        value_class_counts[attr_value][decision] += 1

    # Obliczanie Info(X, T)
    info = 0
    for attr_value, class_counts in value_class_counts.items():
        group_total = sum(class_counts.values())
        group_entropy = entropy_function(class_counts)
        weight = group_total / total_len
        info += weight * group_entropy

    return info


columns = convert_to_columns(r"test\testowaTabDec.txt")

# Convert the file into columns
columns = convert_to_columns(r"test\testowaTabDec.txt")

# Retrieve unique variants of attributes
variants = all_variants_of_attributes(columns)

# Count occurrences of attribute values
attributes_quantit = quantity_of_attributes(columns, variants)

decision_atribute_index = len(columns) - 1 

decision_atribute_entropy = entropy_function(attributes_quantit[decision_atribute_index])


def gain_function():
    decision_atribute = list(columns[decision_atribute_index])
    result_list = {}

    for i in range(len(columns)-1):
    
        info_function_result = info_function(list(columns[i]),decision_atribute)
        diff = decision_atribute_entropy - info_function_result
        result_list[i+1] = diff

    return result_list

