import tkinter as tk
from tkinter import messagebox, filedialog
import service as sc
import csv

def GUI():
    # Function that enables manual addition of products to the catalog
    def gui_add_to_catalog(brand, model, warranty):
        try:
            warranty = int(warranty)
            sc.cursor.execute("INSERT INTO product_catalog (brand, model, warranty_period_months) VALUES (?, ?, ?)",
                              (brand, model, warranty))
            sc.con.commit()
            messagebox.showinfo("Success", "Product added to catalog.")
        except ValueError:
            messagebox.showerror("Error", "Warranty period must be a number!")

    # Function that lists the catalog
    def gui_list_catalog():
        listbox.delete(0, tk.END)
        result = sc.list_catalog()
        for row in result:
            listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]} months")

    # Function that enables selecting a CSV file
    def gui_upload_csv():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            # (Note about UTF-8 BOM encoding preserved as requested)
            with open(file_path, newline='', encoding='utf-8-sig') as file:
                data_list = csv.DictReader(file)
                for row in data_list:
                    brand = row["marka"]
                    model = row["model"]
                    warranty = int(row["garanti_suresi_ay"])
                    sc.add_to_catalog(brand, model, warranty)
            
            gui_list_catalog()
            
        except Exception as e:
            messagebox.showerror("Error", f"CSV could not be loaded:\n{str(e)}")

    # GUI interface
    root = tk.Tk()
    root.title("Product Catalog System")
    root.geometry("400x400")

    tk.Label(root, text="Brand").pack()
    marka_entry = tk.Entry(root)
    marka_entry.pack()

    tk.Label(root, text="Model").pack()
    model_entry = tk.Entry(root)
    model_entry.pack()

    tk.Label(root, text="Warranty Period (Months)").pack()
    garanti_entry = tk.Entry(root)
    garanti_entry.pack()

    tk.Button(root, text="Add to catalog", command=lambda: gui_add_to_catalog(
        marka_entry.get(), model_entry.get(), garanti_entry.get())).pack(pady=5)

    tk.Button(root, text="List catalog", command=gui_list_catalog).pack(pady=5)

    tk.Button(root, text="Upload from CSV", command=gui_upload_csv).pack(pady=5)

    listbox = tk.Listbox(root, width=60)
    listbox.pack(pady=10)

    # Starts the 
    root.mainloop()
