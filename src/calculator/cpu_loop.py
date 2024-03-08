import time

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()

# Kaç kez toplama işlemi yapılacağını belirle
dongu_sayisi = 1000000  # Örnek olarak 1 milyon kez toplama işlemi yapalım

# İşlemi belirtilen sayıda tekrarla
for _ in range(dongu_sayisi):
    toplam = sum(range(1000))  # Örnek olarak, her seferinde 1000 sayısının toplamını alalım

# Bitiş zamanını kaydet
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Hesaplama hızını göster
hesaplama_hizi_ghz = 1 / gecen_sure
print(f"Hesaplama Hızı: {hesaplama_hizi_ghz:.3f} GHz")
