-- Create Database
CREATE DATABASE IF NOT EXISTS supplier_db;
USE supplier_db;

-- Create Suppliers Table
CREATE TABLE IF NOT EXISTS Suppliers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_info TEXT,
    product_categories TEXT
);

-- Create Products Table
CREATE TABLE IF NOT EXISTS Products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    price DECIMAL(10,2),
    category VARCHAR(255),
    description TEXT,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(id) ON DELETE CASCADE
);

-- Insert Data into Suppliers Table
INSERT INTO Suppliers (name, contact_info, product_categories) VALUES 
    ('Supplier A', 'contactA@example.com', 'Laptops, Mobile Phones'),
    ('Supplier B', 'contactB@example.com', 'TVs, Home Appliances'),
    ('Supplier C', 'contactC@example.com', 'Cameras, Accessories');

-- Insert Data into Products Table
INSERT INTO Products (name, brand, price, category, description, supplier_id) VALUES 
    ('Laptop X', 'Brand A', 55000.00, 'Laptops', 'A high-performance laptop', 1),
    ('Smartphone Y', 'Brand B', 20000.00, 'Mobile Phones', 'A budget-friendly smartphone', 1),
    ('LED TV', 'Brand C', 35000.00, 'TVs', 'A 55-inch smart TV', 2),
    ('DSLR Camera', 'Brand D', 45000.00, 'Cameras', 'A professional DSLR camera', 3),
    ('Wireless Headphones', 'Brand E', 5000.00, 'Accessories', 'Noise-canceling headphones', 3);
    
-- Verify Data
SELECT * FROM Suppliers;
SELECT * FROM Products;
