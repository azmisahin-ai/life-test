import torch
import time

# Hücre sayısı
hucre_sayisi = 1  # 40 trilyon hücre

# Ortalama atom sayısı hücre başına (rastgele bir değer)
ortalama_atom_sayisi = 4000000000  # 1 trilyon atom

# Toplam atom sayısı
toplam_atom_sayisi = int(hucre_sayisi * ortalama_atom_sayisi)

print(f"Bir insan vücudundaki toplam atom sayısı: {toplam_atom_sayisi: .2e}")

# 1 milyonda bir durumu simgeliyoruz
olasilik_milyonda_bir = 1e6

# Zamanlayıcı başlatma
baslangic_zamani = time.time()

# Kaç tekrarın kaldığını göstermek için değişken
kalan_tekrar = toplam_atom_sayisi

# PyTorch GPU üzerinde çalışacak şekilde tensöre oluşturma
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Toplam atom sayısı kadar tek bir döngü içinde durumları kontrol etme
for i in range(toplam_atom_sayisi):
    if i % olasilik_milyonda_bir == 0:
        kalan_tekrar -= 1
        gecen_sure = time.time() - baslangic_zamani
        kalan_sure = (gecen_sure / (toplam_atom_sayisi - kalan_tekrar)) * kalan_tekrar

        # Kalan süreyi dakika, saat ve gün cinsinden dönüştürme
        kalan_sure_dakika = kalan_sure / 60
        kalan_sure_saat = kalan_sure_dakika / 60
        kalan_sure_gun = kalan_sure_saat / 24

        print("1 milyonda bir durum gerçekleşti! Geçen Süre: {:.2f} saniye. Kalan Süre: {:.2f} saniye ({:.2f} dakika, {:.2f} saat, {:.2f} gün). Kalan tekrar: {}".format(gecen_sure, kalan_sure, kalan_sure_dakika, kalan_sure_saat, kalan_sure_gun, kalan_tekrar))

    if kalan_tekrar == 0:
        print("Toplam tekrar sayısı kadar durum gerçekleşti.")
        break

# Döngü tamamlandı
print("Döngü tamamlandı. Toplam Geçen Süre: {:.2f} saniye".format(time.time() - baslangic_zamani))
