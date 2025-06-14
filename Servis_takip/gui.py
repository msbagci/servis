import tkinter as tk
from tkinter import messagebox,filedialog
import service as sc
import csv
def GUI():
    #Katalog'a manuel urun eklenmesini saglayan fonksiyon
    def gui_katalog_ekle(marka, model, garanti_suresi):
        try:
            garanti_suresi = int(garanti_suresi)
            sc.cursor.execute("INSERT INTO urun_katalog (marka, model, garanti_suresi_ay) VALUES (?, ?, ?)",
                           (marka, model, garanti_suresi))
            sc.con.commit()
            messagebox.showinfo("Başarılı", "Ürün kataloğa eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Garanti süresi sayı olmalıdır!")
    #Katalog'u gosteren fonksiyon
    def gui_listele_katalog():
        liste.delete(0, tk.END)
        sonuc = sc.listele_katalog()
        for row in sonuc:
            liste.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]} ay")
    #Csv dosyası secilmesini saglayan fonksiyon
    def gui_csv_yukle():
        dosya_yolu = filedialog.askopenfilename(filetypes=[("CSV Dosyaları", "*.csv")])
        if not dosya_yolu:
            return

        try:
            # Dosya UTF-8 BOM (Byte Order Mark) içerebileceğinden, encoding='utf-8-sig' kullanılmıştır.
            with open(dosya_yolu, newline='', encoding='utf-8-sig') as file:
                liste = csv.DictReader(file)
                for row in liste:
                    marka = row["marka"]
                    model = row["model"]
                    garanti = int(row["garanti_suresi_ay"])
                    sc.katalog_ekle(marka, model, garanti)
            gui_listele_katalog()
        except Exception as e:
            messagebox.showerror("Hata", f"CSV yüklenemedi:\n{str(e)}")
        

    #GUI arayuzu
    root = tk.Tk()
    root.title("Ürün Katalog Sistemi")
    root.geometry("400x400")

    # Giriş alanları
    tk.Label(root, text="Marka").pack()
    marka_entry = tk.Entry(root)
    marka_entry.pack()

    tk.Label(root, text="Model").pack()
    model_entry = tk.Entry(root)
    model_entry.pack()

    tk.Label(root, text="Garanti Süresi (Ay)").pack()
    garanti_entry = tk.Entry(root)
    garanti_entry.pack()

    #Butonlar
    tk.Button(root, text="Kataloga ekle", command=lambda: gui_katalog_ekle(
        marka_entry.get(), model_entry.get(), garanti_entry.get())).pack(pady=5)

    tk.Button(root, text="Katalog listele", command=gui_listele_katalog).pack(pady=5)
    tk.Button(root, text="CSV'den Yükle", command=gui_csv_yukle).pack(pady=5)

    #Liste kutusu
    liste = tk.Listbox(root, width=60)
    liste.pack(pady=10)

    #Guı yı calistirir
    root.mainloop()
    
