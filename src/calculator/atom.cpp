#include <iostream>
#include <random>
#include <chrono>

int main() {
    // Hücre sayısı
    long long hucre_sayisi = 40e12;  // 40 trilyon hücre

    // Ortalama atom sayısı hücre başına (rastgele bir değer)
    long long ortalama_atom_sayisi = 1e12;  // 1 trilyon atom

    // Toplam atom sayısı
    long long toplam_atom_sayisi = hucre_sayisi * ortalama_atom_sayisi;

    std::cout << "Bir insan vücudundaki toplam atom sayısı: " << toplam_atom_sayisi << std::endl;

    // 1 milyonda bir durumu simgeliyoruz
    long long olasilik_milyonda_bir = 1e6;
    // 1 milyarda bir durumu simgeliyoruz
    long long olasilik_milyarda_bir = 1e9;
    // 1 trilyonda bir durumu simgeliyoruz
    long long olasilik_trilyonda_bir = 1e12;

    // Zamanlayıcı başlatma
    auto baslangic_zamani = std::chrono::high_resolution_clock::now();

    // Gerçekleşen ve gerçekleşmeyen durumları saymak için değişkenler
    long long gerceklesen_sayisi = 0;
    long long gerceklesen_milyon_sayisi = 0;

    // Kaç tekrarın kaldığını göstermek için değişken
    long long kalan_tekrar = toplam_atom_sayisi;

    // Toplam atom sayısı kadar tek bir döngü içinde durumları kontrol etme
    for (long long i = 0; i < toplam_atom_sayisi; ++i) {
        // Rastgele sayı üretme
        long long random_sayi = rand();

        if (random_sayi % olasilik_milyonda_bir == 0) {
            ++gerceklesen_sayisi;
            --kalan_tekrar;
            std::cout << "1 milyonda bir durum gerçekleşti! Geçen Süre: "
                      << std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - baslangic_zamani).count()
                      << " ms. Kalan tekrar: " << kalan_tekrar << std::endl;
        }

        if (random_sayi % olasilik_milyarda_bir == 0) {
            ++gerceklesen_sayisi;
            --kalan_tekrar;
            std::cout << "1 milyarda bir durum gerçekleşti! Geçen Süre: "
                      << std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - baslangic_zamani).count()
                      << " ms. Kalan tekrar: " << kalan_tekrar << std::endl;
        }

        if (random_sayi % olasilik_trilyonda_bir == 0) {
            ++gerceklesen_sayisi;
            --kalan_tekrar;
            std::cout << "1 trilyonda bir durum gerçekleşti! Geçen Süre: "
                      << std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - baslangic_zamani).count()
                      << " ms. Kalan tekrar: " << kalan_tekrar << std::endl;
        }

        if (kalan_tekrar == 0) {
            std::cout << "Toplam tekrar sayısı kadar durum gerçekleşti." << std::endl;
            break;
        }
    }

    // Gerçekleşmeyen durumları milyon cinsinden yazdırma
    gerceklesen_milyon_sayisi = gerceklesen_sayisi / 1e6;
    std::cout << "Toplam Gerçekleşen Durum Sayısı: " << gerceklesen_milyon_sayisi << " milyon" << std::endl;
    std::cout << "Döngü tamamlandı. Toplam Geçen Süre: "
              << std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - baslangic_zamani).count()
              << " ms" << std::endl;

    return 0;
}
