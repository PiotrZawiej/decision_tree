
from gain_functions import gain_ratio_function

class Node:
    def __init__(self):
        self.test_attribute = None  
        self.children = {}  
        self.class_label = None


def print_tree(node, level=0, prefix=""):
    indent = "      " * level  

    if node.class_label is not None:
        print(f"{indent}{prefix}-> D: {node.class_label}")
    else:
        label = f"{prefix}->Attribute: {node.test_attribute + 1}" if prefix else f"Attribute: {node.test_attribute + 1}"
        print(f"{indent}{label}")
        for value, child in node.children.items():
            print_tree(child, level + 1, str(value))


def is_homogeneous(data):
    decision_column = data[-1]
    return all(value == decision_column[0] for value in decision_column)


def most_common_class(data):
    decision_column = data[-1]
    return max(set(decision_column), key=decision_column.count)


def filter_data_by_value(data, attribute_index, value):
    indices = [i for i, v in enumerate(data[attribute_index]) if v == value]
    return [[column[i] for i in indices] for column in data]


def choose_best_split(data):
    gain_ratios = gain_ratio_function(data)
    if not gain_ratios:
        return None
    return max(gain_ratios, key=gain_ratios.get)


def build_tree(data):
    node = Node()

    if is_homogeneous(data):
        node.class_label = most_common_class(data)
        return node

    best_attribute = choose_best_split(data)
    if best_attribute is None:
        node.class_label = most_common_class(data)
        return node

    node.test_attribute = best_attribute
    unique_values = sorted(set(data[best_attribute]))

    for value in unique_values:
        filtered_data = filter_data_by_value(data, best_attribute, value)

        if filtered_data == data:
            child = Node()
            child.class_label = most_common_class(data)
        elif not filtered_data or len(filtered_data[0]) == 0:
            child = Node()
            child.class_label = most_common_class(data)
        else:
            child = build_tree(filtered_data)

        node.children[value] = child

    return node


