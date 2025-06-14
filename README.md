Bu proje, satışı yapılan ürünlerin takibini yapmak, garanti süresini kontrol etmek ve servis işlemlerini kaydetmek amacıyla geliştirilmiş basit ama işlevsel bir Python uygulamasıdır. Hem komut satırından (terminal arayüzü) hem de grafik kullanıcı arayüzü (GUI) üzerinden kullanılabilir.

proje-klasoru/
├── service.py
├── menu.py
├── gui.py
├── example.csv           ← Örnek ürün kataloğu (sürüm kontrolüne dahil edilmez)
├── .gitignore
├── README.md
└── service.db            ← SQLite veritabanı (çalıştırıldığında otomatik oluşur)


🧩 Dosya Açıklamaları
**service.py**
Uygulamanın veritabanı altyapısını ve iş mantığını içerir.

SQLite kullanılarak 3 tablo oluşturulur:

urun_katalog: Marka, model, garanti süresi gibi bilgiler.

urunler: Satılan ürünlerin satış tarihi ve seri numarası.

servis: Servise gelen ürünler, arıza bilgisi, servis ücreti ve durumu.

Aynı zamanda:

Garanti kontrolü yapılabilir.

Ürün ve servis kayıtları listelenebilir.

Servis durumu güncellenebilir.

CSV dosyasından ürün yüklenebilir (UTF-8-BOM formatında olmalıdır).

**menu.py**
Terminal üzerinden kullanıcı etkileşimini sağlar.

Ana menü sistemi ile:

Ürün ve servis kayıtları eklenebilir.

Garanti durumu sorgulanabilir.

Servis durumu güncellenebilir.

GUI açılabilir.

**gui.py**
Grafiksel kullanıcı arayüzünü içerir (örnek: Tkinter ile hazırlanmış olabilir).

Arayüz üzerinden ürün ekleme, listeleme ve sorgulama işlemleri yapılabilir.

Detaylı bilgi GUI kodu incelenerek görülebilir.

katalog.csv
Örnek bir ürün kataloğu içeren dosyadır.

Kullanıcılara nasıl toplu veri aktarımı yapılacağı gösterilir.

Git versiyon kontrolüne dahil edilmez (.gitignore içinde dışlanmıştır).

**service.db**
SQLite veritabanı dosyasıdır.

Uygulama ilk çalıştırıldığında otomatik olarak oluşturulur.

Tüm ürün ve servis bilgileri bu dosyada saklanır.

⚙️ Özellikler
Garanti Kontrolü: Ürünlerin garanti süresi, satış tarihine göre otomatik hesaplanır.

Ücretlendirme: Garanti süresi geçmişse servis ücreti girilir, aksi takdirde 0 olarak kaydedilir.

Servis Durumu: "Serviste" veya "Tamamlandı" gibi bilgiler kayıt altına alınır.

CSV Desteği: Dış kaynaklı ürün verileri kolayca içe aktarılabilir.

GUI: Komut satırına ek olarak görsel arayüzle de kullanım imkânı.

🔒 **.gitignore** Dosyası
Projede yer alan .gitignore dosyası, aşağıdaki dosya ve klasörlerin Git tarafından izlenmemesini sağlar:

__pycache__/, *.pyc: Derleme önbellekleri

*.db: SQLite veritabanı dosyaları (kişisel ve dinamik veriler içerdiği için)

example.csv: Kullanıcıya özel örnek veriler içerebilir

Bu dosya sayesinde repoya gereksiz veya kişisel verilerin dahil edilmesi engellenir.

Gereksinimler
Python 3.7 veya üzeri

Gerekli kütüphaneler:

pip install python-dateutil


📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
Lisans, bu projenin özgürce kullanılmasına, değiştirilmesine ve dağıtılmasına izin verir. Ancak, yazılım “olduğu gibi” sağlanır ve herhangi bir garanti sunulmaz.

Ayrıntılı bilgi için  ([LICENSE](LICENSE) dosyasını inceleyebilirsiniz.
