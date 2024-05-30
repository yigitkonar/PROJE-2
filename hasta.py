from datetime import datetime

class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    # Get metotları
    def get_hasta_no(self):
        return self.__hasta_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def get_tedavi(self):
        return self.__tedavi

    # Set metotları
    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik


    # Tedavi süresi hesaplama metodu
    # Hastalık tedavi süreleri rastgele verildi
    def tedavi_suresi_hesapla(self):
        hastalik_tedavi_sureleri = {
            "Yüksek Tansiyon": 20,
            "Grip": 10,
            "Kanser": 180 }

        return hastalik_tedavi_sureleri.get(self.__hastalik, "Bilinmiyor")

    # __str__ metodu
    def __str__(self):
        return (f"Hasta No: {self.__hasta_no}, "
                f"Ad: {self.__ad}, "
                f"Soyad: {self.__soyad}, "
                f"Doğum Tarihi: {self.__dogum_tarihi}, "
                f"Hastalık: {self.__hastalik}, "
                f"Tedavi: {self.__tedavi}")

    # Bilgileri göster
    def bilgileri_goster(self):
        print(self.__str__())
        print(f"Tedavi Süresi: {self.tedavi_suresi_hesapla()} gün")

