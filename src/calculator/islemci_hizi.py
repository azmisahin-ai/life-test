import time

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()

# Bir miktar matematiksel işlem yapalım
result = 0
for _ in range(1000000):  # Örnek olarak, 1 milyon kez basit bir işlemi tekrar edelim
    result += 1

# Bitiş zamanını kaydet
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Hesaplama hızını göster
hesaplama_hizi_ghz = 1 / gecen_sure
print(f"Işlemci Hızı: {hesaplama_hizi_ghz:.3f} GHz")
