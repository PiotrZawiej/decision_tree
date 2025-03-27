import math

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
