from file_atributes import convert_to_columns, quantity_of_attributes, all_variants_of_attributes
from Entropy import entropy_function, info_function


columns = convert_to_columns(r"test\car.data")

# Retrieve unique variants of attributes
variants = all_variants_of_attributes(columns)

# Count occurrences of attribute values
attributes_quantit = quantity_of_attributes(columns, variants)

decision_atribute_index = len(columns) - 1 

decision_atribute_entropy = entropy_function(attributes_quantit[decision_atribute_index])


def gain_function(column):
    decision_atribute = list(column[decision_atribute_index])
    result_list = {}

    for i in range(len(column)):
        if i == decision_atribute_index:
            continue  

        info_result = info_function(list(column[i]), decision_atribute)
        diff = decision_atribute_entropy - info_result
        result_list[i] = diff  

    return result_list


def gain_ratio_function(column):
    result_list = {}
    gain_values = gain_function(column)

    for i in range(len(column)):
        if i == decision_atribute_index:
            continue 

        attr_col = list(column[i])
        gain = gain_values[i]
        value_counts = {}
        for val in attr_col:
            value_counts[val] = value_counts.get(val, 0) + 1

        split_info = entropy_function(value_counts)
        gain_ratio = gain / split_info if split_info != 0 else 0
        result_list[i] = gain_ratio

    return result_list


    