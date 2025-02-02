import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row  # Store the entire row as a list
    
    return dictionary

def main():
    products_dict = read_dictionary('products.csv', 0)
    print("All Products")
    print(products_dict)
    
    with open('request.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        print("\nRequested Items")
        
        for row in reader:
            product_number, quantity = row
            quantity = int(quantity)
            
            if product_number in products_dict:
                product_name = products_dict[product_number][1]
                product_price = products_dict[product_number][2]
                print(f"{product_name}: {quantity} @ {product_price}")
            else:
                print(f"Error: Product {product_number} not found in catalog.")

main()
