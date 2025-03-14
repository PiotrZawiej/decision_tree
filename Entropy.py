import math

def attributes_probability(attributes_quantit, all_attributes_quantit):

    probabilities = []

    for quantit_list in attributes_quantit:
        probability_dict = {}

        for key, value in quantit_list.items():
            probability_dict[key] = value / all_attributes_quantit
        
        probabilities.append(probability_dict)

    return probabilities


def entropy_function(probability):

    decision_argument = len(probability) - 1
    entropy = 0

    for key in probability[decision_argument]:
        p = probability[decision_argument][key]
        if p > 0:
            entropy += (p * math.log2(p))

    return -entropy
