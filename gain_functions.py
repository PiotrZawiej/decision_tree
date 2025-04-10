import math
from file_atributes import convert_to_columns, quantity_of_attributes, all_variants_of_attributes
from Entropy import entropy_function, info_function


columns = convert_to_columns(r"test\test2.txt")

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


def gain_ratio_function():
    result_list = {}

    gain_values = gain_function()

    for i in range(len(columns) - 1):
        attr_col = list(columns[i])
        gain = gain_values[i + 1]  
        value_counts = {}
        for val in attr_col:
            value_counts[val] = value_counts.get(val, 0) + 1

        split_info = entropy_function(value_counts)

        if split_info == 0:
            gain_ratio = 0
        else:
            gain_ratio = gain / split_info

        result_list[i + 1] = gain_ratio

    return result_list
    