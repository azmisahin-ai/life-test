import numpy as np
import time

baslangic_zamani = time.time()
toplam = 1000000000
olasilik = 1000000

data = np.arange(toplam)

for i in range(toplam):
    if i % olasilik == 0:
        bitis_zamani = time.time()
        gecen_sure = bitis_zamani - baslangic_zamani
        if gecen_sure != 0:
            hesaplama_hizi_ghz = 1 / gecen_sure
            print(f"Işlemci Hızı: {hesaplama_hizi_ghz:.3f} GHz")
