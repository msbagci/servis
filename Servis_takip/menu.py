import service as sc
from datetime import datetime
import gui

# Function that runs functions in the terminal
def menu():
    while True:
        print("\n--- Welcome! Please select the action you would like to take. ---")
        print("1. Add product to the catalog")
        print("2. Add a sold item")
        print("3. List products")
        print("4. Check product warranty")
        print("5. Add Product to Service")
        print("6. View service records")
        print("7. List catalog")
        print("8. Add product from CSV")
        print("9. Update service status")
        print("0. GUI")
        print("e. Exit")

        choice = input("Choice: ")

        if choice == "1":
            brand = input("Brand: ")
            model = input("Model: ")
            warranty = input("Warranty Period (Month): ")
            if not warranty.isdigit():
                print("Warranty period must be a number!")
                continue
            sc.add_to_catalog(brand, model, int(warranty))
            print("The product has been added to the catalog.")

        elif choice == "2":
            catalog_id = input("Catalog ID: ")
            sell_date = input("Sell Date (YYYY-MM-DD): ")
            serial_number = input("Serial No: ")
            try:
                datetime.strptime(sell_date, "%Y-%m-%d")
            except ValueError:
                print("Date format is incorrect!")
                continue
            sc.add_sold_product(int(catalog_id), sell_date, serial_number)
            print("Sold item added.")

        elif choice == "3":
            print("\n--- Sold Products ---")
            sc.list_products()

        elif choice == "4":
            product_id = input("ID of the product whose warranty status you want to check: ")
            sc.check_warranty_status(int(product_id))
            
        elif choice == "5":
            product_id = input("Product ID: ")
            fault_description = input("Fault Description: ")
            try:
                fee = float(input("Fee (0 if under warranty): "))
            
            except ValueError:
                print("Invalid fee")
                continue
            
            sc.add_to_service(int(product_id), fault_description, fee)
            print("Service record added.")
        
        elif choice == "6":
            print("\n--- Service Records ---")
            sc.list_service_records()
        
        elif choice == "7":
            print("Products in Catalog\n")
            [print(product) for product in sc.list_catalog()]
        
        elif choice == "8":
            file_name = input("Select file: ")
            sc.add_catalog_from_csv(file_name)
            
        
        elif choice == "9":
            service_id = input("Enter Service ID: ")
            sc.update_service_status(int(service_id))

        elif choice == "0":
            gui.GUI()

        elif choice.lower() == "e":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1-9.")

if __name__ == "__main__":
    menu()
