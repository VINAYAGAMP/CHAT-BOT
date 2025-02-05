import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this if you have a different MySQL username
    password="123",  # Change to your MySQL password
    database="supplier_db"
)

cursor = conn.cursor()

# Function to fetch all suppliers
def fetch_suppliers():
    cursor.execute("SELECT * FROM Suppliers")
    suppliers = cursor.fetchall()
    print("\n--- Suppliers ---")
    for supplier in suppliers:
        print(f"ID: {supplier[0]}, Name: {supplier[1]}, Contact: {supplier[2]}, Categories: {supplier[3]}")

# Function to fetch all products
def fetch_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    print("\n--- Products ---")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Brand: {product[2]}, Price: {product[3]}, Category: {product[4]}, Description: {product[5]}, Supplier ID: {product[6]}")

# Function to insert a new supplier
def add_supplier(name, contact_info, product_categories):
    query = "INSERT INTO Suppliers (name, contact_info, product_categories) VALUES (%s, %s, %s)"
    values = (name, contact_info, product_categories)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Supplier added successfully!")

# Function to insert a new product
def add_product(name, brand, price, category, description, supplier_id):
    query = "INSERT INTO Products (name, brand, price, category, description, supplier_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, brand, price, category, description, supplier_id)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Product added successfully!")

# Function to delete a supplier by ID
def delete_supplier(supplier_id):
    query = "DELETE FROM Suppliers WHERE id = %s"
    cursor.execute(query, (supplier_id,))
    conn.commit()
    print("✅ Supplier deleted successfully!")

# Function to delete a product by ID
def delete_product(product_id):
    query = "DELETE FROM Products WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    print("✅ Product deleted successfully!")

# Menu for user interaction
while True:
    print("\n--- Supplier & Product Management ---")
    print("1. View Suppliers")
    print("2. View Products")
    print("3. Add Supplier")
    print("4. Add Product")
    print("5. Delete Supplier")
    print("6. Delete Product")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        fetch_suppliers()
    elif choice == "2":
        fetch_products()
    elif choice == "3":
        name = input("Enter Supplier Name: ")
        contact_info = input("Enter Contact Info: ")
        categories = input("Enter Product Categories: ")
        add_supplier(name, contact_info, categories)
    elif choice == "4":
        name = input("Enter Product Name: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        supplier_id = int(input("Enter Supplier ID: "))
        add_product(name, brand, price, category, description, supplier_id)
    elif choice == "5":
        supplier_id = int(input("Enter Supplier ID to delete: "))
        delete_supplier(supplier_id)
    elif choice == "6":
        product_id = int(input("Enter Product ID to delete: "))
        delete_product(product_id)
    elif choice == "7":
        print("Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1-7.")

# Close MySQL connection
conn.close()
import json

# Sample data
data = {
    "Suppliers": [
        {"id": 1, "name": "Supplier A", "contact_info": "contactA@example.com", "product_categories": "Laptops, Mobile Phones"},
        {"id": 2, "name": "Supplier B", "contact_info": "contactB@example.com", "product_categories": "TVs, Home Appliances"}
    ],
    "Products": [
        {"id": 1, "name": "Laptop X", "brand": "Brand A", "price": 55000.00, "category": "Laptops", "description": "A high-performance laptop", "supplier_id": 1},
        {"id": 2, "name": "Smartphone Y", "brand": "Brand B", "price": 20000.00, "category": "Mobile Phones", "description": "A budget-friendly smartphone", "supplier_id": 1},
        {"id": 3, "name": "LED TV", "brand": "Brand C", "price": 35000.00, "category": "TVs", "description": "A 55-inch smart TV", "supplier_id": 2}
    ]
}

# Save to JSON file
with open("supplier_data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read from JSON file
with open("supplier_data.json", "r") as file:
    loaded_data = json.load(file)

# Display products
print("\nProduct List:")
for product in loaded_data["Products"]:
    print(product)
