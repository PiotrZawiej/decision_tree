import math

def attributes_probability(attributes_quantit, all_attributes_quantit):

    probabilities = []

    for quantit_list in attributes_quantit:
        probability_dict = {}

        for key, value in quantit_list.items():
            probability_dict[key] = value / all_attributes_quantit
        
        probabilities.append(probability_dict)

    return probabilities


def entropy_function(atribute, probability):

    entropy = 0

    for key in probability[atribute]:
        p = probability[atribute][key]
        if p > 0:
            entropy += (p * math.log2(p))

    return -entropy


# def entropy_by_decison_class_function(atribute, atrubust_quantit):
    
#     decision_class = atrubust_quantit[atribute]
#     values_quantit = sum(decision_class.values())
#     info_function = 0
    
#     return_list = []
    
#     for value in decision_class.values():
#         return_list.append(value/values_quantit)
        
    
#     return return_list
