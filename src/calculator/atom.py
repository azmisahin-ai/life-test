import time

# Hücre sayısı
hucre_sayisi = 40e12  # 40 trilyon hücre

# Ortalama atom sayısı hücre başına (rastgele bir değer)
ortalama_atom_sayisi = 1e12  # 1 trilyon atom

# Toplam atom sayısı
toplam_atom_sayisi = int(hucre_sayisi * ortalama_atom_sayisi)

print(f"Bir insan vücudundaki toplam atom sayısı: {toplam_atom_sayisi: .2e}")

# 1 milyonda bir durumu simgeliyoruz
olasilik_milyonda_bir = 1e6

# Zamanlayıcı başlatma
baslangic_zamani = time.time()

# Kaç tekrarın kaldığını göstermek için değişken
kalan_tekrar = toplam_atom_sayisi

# Toplam atom sayısı kadar tek bir döngü içinde durumları kontrol etme
for i in range(toplam_atom_sayisi):
    if i % olasilik_milyonda_bir == 0:
        kalan_tekrar -= 1
        print("1 milyonda bir durum gerçekleşti! Geçen Süre: {:.2f} saniye. Kalan tekrar: {}".format(time.time() - baslangic_zamani, kalan_tekrar))

    if kalan_tekrar == 0:
        print("Toplam tekrar sayısı kadar durum gerçekleşti.")
        break

# Döngü tamamlandı
print("Döngü tamamlandı. Toplam Geçen Süre: {:.2f} saniye".format(time.time() - baslangic_zamani))
