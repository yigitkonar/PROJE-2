from personel import Personel

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # Get metotları
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    # SEt metotları
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Maaşı arttırma metodu
    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (1.5 + oran / 100)
        self.set_maas(yeni_maas)

    # __str__ metodu
    def __str__(self):
        personel_str = super().__str__()
        return (f"{personel_str}, Uzmanlık: {self.__uzmanlik}, "
                f"Deneyim Yılı: {self.__deneyim_yili}, "
                f"Hastane: {self.__hastane}")

    # Bilgileri göster
    def bilgileri_goster(self):
        print(self.__str__())
