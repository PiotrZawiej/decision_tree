
def read_file(file):

    with open(file, "r") as f:
        lines = f.readlines()
        return lines


def convert_to_columns():

    result = []
    for x in read_file(r"test\testowaTabDec.txt"):
        if x.strip(): 
            result.append(x.strip().split(','))  

    columns = list(zip(*result))

    return(columns)


def all_variants_of_atributs(columns):

    variants = []

    for column in columns:
        uniqe_values = list(set(column))
        variants.append(uniqe_values)

    return variants


def quantity_of_attributes(columns, variants):
    counts = []  

    for col_values, col_variants in zip(columns, variants):  
        count_dict = {}  

        for variant in col_variants:
            count_dict[variant] = col_values.count(variant)  

        counts.append(count_dict)  

    return counts


