from gain_functions import  gain_function, gain_ratio_function
from file_atributes import convert_to_columns
from decision_tree import build_tree, print_tree

def main():
    
    columns = convert_to_columns(r"test\car.data")
    r = gain_ratio_function(columns)
    tree = build_tree(columns)
    print_tree(tree)
    
if __name__ == "__main__":
    main()