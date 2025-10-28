import sqlite3
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Database connection
con = sqlite3.connect("service.db")
cursor = con.cursor()

# Catalog table
cursor.execute("""
CREATE TABLE IF NOT EXISTS product_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    warranty_period_months INTEGER NOT NULL
               
)
""")

# Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    catalog_id INTEGER,
    sell_date TEXT NOT NULL,
    serial_number TEXT NOT NULL,
    FOREIGN KEY (catalog_id) REFERENCES product_catalog(id)
)
""")

# Service table
cursor.execute("""
CREATE TABLE IF NOT EXISTS service_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    fault_description TEXT NOT NULL,
    status TEXT NOT NULL,
    fee REAL NOT NULL,
    service_status TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

con.commit()

# Function that adds new products to the catalog
def add_to_catalog(brand, model, warranty_period_months):
    cursor.execute("INSERT INTO product_catalog (brand, model, warranty_period_months) VALUES (?, ?, ?)",
                   (brand, model, warranty_period_months))
    con.commit()

# Function that adds sold products to the products list
def add_sold_product(catalog_id, sell_date, serial_number):
    cursor.execute("INSERT INTO products (catalog_id, sell_date, serial_number) VALUES (?, ?, ?)",
                   (catalog_id, sell_date, serial_number))
    con.commit()

# Function that checks if the entered product ID is under warranty
def check_warranty_status(product_id):
    cursor.execute("""
    SELECT sell_date, warranty_period_months FROM products
    JOIN product_catalog ON products.catalog_id = product_catalog.id
    WHERE products.id = ?
    """, (product_id,))
    result = cursor.fetchone()
    
    if not result:
        print("Product not found.")
        return False
    
    
    sell_date_str, warranty_period_months = result
    sell_date = datetime.strptime(sell_date_str, "%Y-%m-%d")
    warranty_end_date = sell_date + relativedelta(months=+warranty_period_months)
    
    if datetime.now() <= warranty_end_date:
        print("Under warranty.")
        return True
    else:
        print("Warranty period expired.")
        return False

# Function that enables adding a product to the service
def add_to_service(product_id, fault_description, fee):
    # check_warranty_status returns True if under warranty
    if check_warranty_status(product_id):
        status = "Warrantied"
        fee = 0  # Fee set to 0 if under warranty
    else:
        status = "Out of Warranty"
    
    cursor.execute("INSERT INTO service_records (product_id, fault_description, status, fee, service_status) VALUES (?, ?, ?, ?, ?)",
    (product_id, fault_description, status, fee, "In Service"))
    con.commit()

# Function that lists products in the catalog 
def list_catalog():
    cursor.execute("SELECT * FROM product_catalog")
    return cursor.fetchall()

# Function that lists sold products
def list_products():
    cursor.execute("""
    SELECT products.id, brand, model, sell_date, serial_number FROM products
    JOIN product_catalog ON products.catalog_id = product_catalog.id
    """)
    for row in cursor.fetchall():
        print(row)

# Function that lists products in service
def list_service_records():
    cursor.execute("SELECT * FROM service_records")
    for row in cursor.fetchall():
        print(row)

# Function to update the service status
def update_service_status(service_id):
    cursor.execute("""
    UPDATE service_records
    SET service_status = 'Completed'
    WHERE id = ?
    """, (service_id,))
    con.commit()
    # Service status updated to Completed
    print("Service status updated to Completed")

# Function that enables adding a catalog via CSV file
def add_catalog_from_csv(file_name):
    try:
        with open(file_name, newline="", encoding="utf-8-sig") as csvfile:
            product_list = csv.DictReader(csvfile)
            products_to_add = list(product_list)
        
        for row in products_to_add:
            brand = row["marka"]
            model = row["model"]
            try:
                warranty = int(row["garanti_suresi_ay"])
            except ValueError:
                print(f"Invalid warranty period: {row['garanti_suresi_ay']}")
                continue
            
            add_to_catalog(brand, model, warranty)
        
        print("Catalog added")
        
    except FileNotFoundError:

        print("CSV file not found")
    except KeyError as e:

        print(f"Invalid value:{e}")
