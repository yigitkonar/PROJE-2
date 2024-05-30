from personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    # Get metotları
    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane

    # Set metotları
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # __str__ metodu
    def __str__(self):
        personel_str = super().__str__()
        return (f"{personel_str}, Çalışma Saati: {self.__calisma_saati}, "
                f"Sertifika: {self.__sertifika}, "
                f"Hastane: {self.__hastane}")

    # Maaşı arttırma metodu
    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (1 + oran / 100)
        self.set_maas(yeni_maas)

    # Bilgileri göster metodu
    def bilgileri_goster(self):
        print(self.__str__())

