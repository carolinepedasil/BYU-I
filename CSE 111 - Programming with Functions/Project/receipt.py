import csv
from datetime import datetime, timedelta

def load_products(filename):
    products = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_id, name, price = row
                products[product_id] = {'name': name, 'price': float(price)}
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e:
        print("Error: permission denied when accessing the file.")
        print(e)
        exit()
    return products

def process_request(products, filename):
    items = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_id, quantity = row
                if product_id not in products:
                    raise KeyError(product_id)
                product = products[product_id]
                items.append({
                    'name': product['name'],
                    'quantity': int(quantity),
                    'price': product['price'],
                    'total': int(quantity) * product['price']
                })
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e:
        print("Error: permission denied when accessing the file.")
        print(e)
        exit()
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)
        exit()
    return items

def print_receipt(items):
    store_name = "Inkom Emporium"
    sales_tax_rate = 0.06
    total_quantity = sum(item['quantity'] for item in items)
    subtotal = sum(item['total'] for item in items)
    sales_tax = round(subtotal * sales_tax_rate, 2)
    total = round(subtotal + sales_tax, 2)
    
    print(store_name)
    for item in items:
        print(f"{item['name']}: {item['quantity']} @ {item['price']:.2f}")
    print(f"Number of Items: {total_quantity}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at the Inkom Emporium.")
    
    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %d %I:%M:%S %Y"))
    
    # Exceeds requirements: Print return by date (30 days from now)
    return_date = current_date_and_time + timedelta(days=30)
    print(f"Return by: {return_date.strftime('%a %b %d 09:00 PM %Y')}")
    
    # Exceeds requirements: Days until New Year's Sale
    new_year = datetime(current_date_and_time.year + 1, 1, 1)
    days_until_sale = (new_year - current_date_and_time).days
    print(f"Only {days_until_sale} days until our New Year's Sale!")

if __name__ == "__main__":
    products = load_products("products.csv")
    items = process_request(products, "request.csv")
    print_receipt(items)
