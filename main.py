from file_atributes import all_variants_of_attributes, quantity_of_attributes, convert_to_columns, read_file
from Entropy import  entropy_function, info_function

def main():
    # Convert the file into columns
    columns = convert_to_columns(r"test\testowaTabDec.txt")
    
    # Retrieve unique variants of attributes
    variants = all_variants_of_attributes(columns)
    
    # Count occurrences of attribute values
    attributes_quantit = quantity_of_attributes(columns, variants)

    # Compute and print entropy    
    # entropy = entropy_function(attributes_quantit[0])
    # print(entropy)

    decision_atribute_index = len(columns) - 1 
    decision_atribute = list(columns[decision_atribute_index])

    for i in range(len(columns)-1):
    
        info_function_result = info_function(list(columns[i]),decision_atribute)
        print(info_function_result)


    
if __name__ == "__main__":
    main()