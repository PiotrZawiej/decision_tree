from file_atributes import all_variants_of_atributs, quantity_of_attributes, convert_to_columns

columns = convert_to_columns()
variants = all_variants_of_atributs(columns)
attributes_quantit = quantity_of_attributes(columns, variants)

print(variants)
print(attributes_quantit)