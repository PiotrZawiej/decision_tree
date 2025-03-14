from file_atributes import all_variants_of_attributes, quantity_of_attributes, convert_to_columns, read_file
from Entropy import attributes_probability, entropy_function

def main():
    # Convert the file into columns
    columns = convert_to_columns(r"test\testowaTabDec.txt")
    
    # Retrieve unique variants of attributes
    variants = all_variants_of_attributes(columns)
    
    # Count occurrences of attribute values
    attributes_quantit = quantity_of_attributes(columns, variants)
    
    # Get the total number of attributes (rows)
    all_attributes = len(read_file(r"test\testowaTabDec.txt"))
    
    # Calculate probabilities for attribute values
    probability = attributes_probability(attributes_quantit, all_attributes)

    # Compute and print entropy
    entropy = entropy_function(probability)
    print(f"Entropy is equal to {entropy}")

if __name__ == "__main__":
    main()