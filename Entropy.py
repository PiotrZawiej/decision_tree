from file_atributes import all_variants_of_attributes, quantity_of_attributes, convert_to_columns, read_file

columns = convert_to_columns(r"test\testowaTabDec.txt")
variants = all_variants_of_attributes(columns)
attributes_quantit = quantity_of_attributes(columns, variants)


def Entropy_function(attributes_quantit, all_attributes_quantit):

    for quantit_list in attributes_quantit:
        for key, item in quantit_list.items():
            quantit_list[key] = quantit_list[key] / all_attributes_quantit

    return attributes_quantit

all_attributes = len(read_file(r"test\testowaTabDec.txt"))
print(Entropy_function(attributes_quantit, all_attributes))

