import time

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()

# Bir döngü içinde basit bir işlemi tekrarlayalım
for _ in range(1000000):  # Örnek olarak, 1 milyon kez basit bir işlemi tekrar edelim
    result = sum(range(1000))  # Her seferinde 1000 sayısının toplamını alalım

# Bitiş zamanını kaydet
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Döngü hızını göster
dongu_hizi = 1 / gecen_sure
print(f"Döngü Hızı: {dongu_hizi:.3f} döngü/saniye")
