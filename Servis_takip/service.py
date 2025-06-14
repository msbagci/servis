import sqlite3
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

con = sqlite3.connect("service.db")
cursor = con.cursor()

#Katalog tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS urun_katalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marka TEXT NOT NULL,
    model TEXT NOT NULL,
    garanti_suresi_ay INTEGER NOT NULL
)
""")
#Urunler tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS urunler (
    id_ INTEGER PRIMARY KEY AUTOINCREMENT,
    katalog_id INTEGER,
    satis_tarihi TEXT NOT NULL,
    seri_no TEXT NOT NULL,
    FOREIGN KEY (katalog_id) REFERENCES urun_katalog(id)
)
""")

#Servis tablosu
cursor.execute("""
CREATE TABLE IF NOT EXISTS servis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    urun_id INTEGER NOT NULL,
    ariza TEXT NOT NULL,
    durum TEXT NOT NULL,
    ucret REAL NOT NULL,
    servis_durumu TEXT NOT NULL,
    FOREIGN KEY (urun_id) REFERENCES urunler(id_)
    
)
""")

con.commit()
#Katalog'a yeni urun eklenilmesini saglayan fonksiyon
def katalog_ekle(marka, model, garanti_suresi_ay):
    cursor.execute("INSERT INTO urun_katalog (marka, model, garanti_suresi_ay) VALUES (?, ?, ?)",
                   (marka, model, garanti_suresi_ay))
    con.commit()
#Satilan urunleri urunler listesine ekleyen fonksiyon
def urun_ekle(katalog_id, satis_tarihi, seri_no):
    cursor.execute("INSERT INTO urunler (katalog_id, satis_tarihi, seri_no) VALUES (?, ?, ?)",
                   (katalog_id, satis_tarihi, seri_no))
    con.commit()
#Id'si girilen urunun garantisi olup olmadigini kontrol eden fonksiyon
def garanti_durumu(urun_id):
    cursor.execute("""
    SELECT satis_tarihi, garanti_suresi_ay FROM urunler
    JOIN urun_katalog ON urunler.katalog_id = urun_katalog.id
    WHERE urunler.id_ = ?
    """, (urun_id,))
    result = cursor.fetchone()
    if not result:
        print("Urun bulunamadı.")
        return False
    satis_tarihi_str, garanti_suresi_ay = result
    satis_tarihi = datetime.strptime(satis_tarihi_str, "%Y-%m-%d")
    garanti_bitis = satis_tarihi + relativedelta(months=+garanti_suresi_ay)
    if datetime.now() <= garanti_bitis:
        print("Garanti kapsamında.")
        return True
    else:
        print("Garanti suresi dolmus.")
        return False
#Servise urun eklenilmesini saglayan fonksiyon
def servis_ekle(urun_id, ariza, ucret):
    if garanti_durumu(urun_id):
        durum = "Garantili"
        ucret = 0
    else:
        durum = "Garanti Dısı"
    cursor.execute("INSERT INTO servis (urun_id, ariza, durum, ucret, servis_durumu) VALUES (?, ?, ?, ?, ?)",
    (urun_id, ariza, durum, ucret, "Serviste"))
    con.commit()
#Katalogdaki urunleri listeleyen fonksiyon
def listele_katalog():
    cursor.execute("SELECT * FROM urun_katalog")
    return cursor.fetchall()
#Satılan urunleri listeleyen fonksiyon
def listele_urunler():
    cursor.execute("""
    SELECT urunler.id_, marka, model, satis_tarihi, seri_no FROM urunler
    JOIN urun_katalog ON urunler.katalog_id = urun_katalog.id
    """)
    for row in cursor.fetchall():
        print(row)
#Servisteki urunleri listeleyen fonksiyon
def listele_servisler():
    cursor.execute("SELECT * FROM servis")
    for row in cursor.fetchall():
        print(row)
def servis_guncelleme(servis_id):
    cursor.execute("""
    UPDATE servis
    SET servis_durumu = 'Tamamlandı'
    WHERE id = ?
    """, (servis_id,))
    con.commit()
    print("Servis durumu tamalandı olarak guncellendi")
    
    
#csv dosyası ile katalog eklenmesini saglayan fonksiyon
def csv_katalog_ekle(dosya_adi):
    try:
        with open(dosya_adi,newline="",encoding="utf-8-sig") as csvfile:
            liste = csv.DictReader(csvfile)
            urunler = list(liste)
        for satir in urunler:
            marka = satir["marka"]
            model = satir["model"]
            try:
                garanti = int(satir["garanti_suresi_ay"])
            except ValueError:
                print(f"gecersiz garanti suresi: {satir['garanti_suresi_ay']}")
                continue
            katalog_ekle(marka,model,garanti)
        print("Katalog eklendi")
    except FileNotFoundError:
        print("CSV dosyası bulunamadı")
    except KeyError as e:
        print(f"geçersiz değer:{e}")



