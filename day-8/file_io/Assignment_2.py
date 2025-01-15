# # Use the csv module to:
# # Write product details (name, price, stock) into a CSV file.
# # Read the file back and print the products sorted by price.
import csv
def write(file):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Stock'])
        while True:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            writer.writerow([name, price, stock])
            user_input = input("Do you want to stop adding product? (Type 'QUIT' to stop/Enter to continue): ").strip().lower()
            if user_input == 'quit':
                break

def read(file):
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        sorted_items = sorted(reader, key=lambda row: float(row['Price']))
        for item in sorted_items:
            print(item)
            
file_name = 'mobiles.csv'
write(file_name)
read(file_name)