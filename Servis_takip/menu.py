import service as sc
from datetime import datetime
import gui
#Fonksiyonlari terminalde calistiran fonksiyon
def menu():
    while True:
        print("\n--- Hos geldiniz lutfen yapmak istediginiz islemi seciniz ---")
        print("1. Kataloga urun ekle")
        print("2. Satılan urun ekle")
        print("3. Urunleri listele")
        print("4. Urun garantisini kontrol et")
        print("5. Servise Ürün Ekle")
        print("6. Servis kayıtlarını listele")
        print("7. Katalogu listele")
        print("8. Csv den urun ekle")
        print("9. Servis durumunu guncelle")
        print("0. GUI")
        print("e. Cikis")

        secim = input("Seciminiz: ")

        if secim == "1":
            marka = input("Marka: ")
            model = input("Model: ")
            garanti = input("Garanti Süresi (Ay): ")
            if not garanti.isdigit():
                print("Garanti süresi sayı olmalı!")
                continue
            sc.katalog_ekle(marka, model, int(garanti))
            print("Ürün kataloğa eklendi.")

        elif secim == "2":
            katalog_id = input("Katalog ID: ")
            satis_tarihi = input("Satış Tarihi (YYYY-AA-GG): ")
            seri_no = input("Seri No: ")
            try:
                datetime.strptime(satis_tarihi, "%Y-%m-%d")
            except ValueError:
                print("Tarih formatı hatalı!")
                continue
            sc.urun_ekle(int(katalog_id), satis_tarihi, seri_no)
            print("Satılan ürün eklendi.")

        elif secim == "3":
            print("\n--- Satılan Urunler ---")
            sc.listele_urunler()

        elif secim == "4":
            urun_id = input("Garanti durumunu kontrol etmek istediğiniz ürünün ID'si: ")
            sc.garanti_durumu(int(urun_id))
        
        elif secim == "5":
            urun_id = input("urun id: ")
            ariza = input("ariza: ")
            try:
                ucret = float(input("ucret (eğer garanti kapsamındaysa 0 olacak): "))
            except ValueError:
                print("gecersiz ucret")
                continue
            sc.servis_ekle(int(urun_id), ariza, ucret)
            print("servis kaydı eklendi.")
        elif secim == "6":
            print("\n--- Servis Kayıtları ---")
            sc.listele_servisler()
       
        elif secim == "7":
            print("Katalogdaki urunler\n")
            [print(urun) for urun in sc.listele_katalog()]
        elif secim == "8":
            dosya = input("Dosya seciniz: ")
            sc.csv_katalog_ekle(dosya)
        elif secim == "9":
            servis_id = input("Servis id'girin: ")
            sc.servis_guncelleme(int(servis_id))
        elif secim == "0":
            gui.GUI()
        elif secim.lower() == "e":
             print("Cıkılıyor...")
             break
        
        else:
            print("Gecersiz secim! lutfen 1-9 arası bir sayı girin.")

if __name__ == "__main__":
    menu()