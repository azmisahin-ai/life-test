import time

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()

# Hızlı bir matematik işlemi yapalım, örneğin 10 milyon sayının toplamını alalım
toplam = sum(range(10_000_000))

# Bitiş zamanını kaydet
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Hesaplama hızını göster
print(f"Hesaplama hızı: {gecen_sure:.6f} saniye")
## Hesaplama hızı: 0.227324 saniye