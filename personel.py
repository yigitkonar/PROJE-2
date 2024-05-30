class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    # Get metotları
    def get_personel_no(self):
        return self.__personel_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_departman(self):
        return self.__departman

    def get_maas(self):
        return self.__maas

    # Set metotları
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no

    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_departman(self, departman):
        self.__departman = departman

    def set_maas(self, maas):
        self.__maas = maas

    # __str__ metodu
    def __str__(self):
        return (f"Personel No: {self.__personel_no}, "
                f"Ad: {self.__ad}, "
                f"Soyad: {self.__soyad}, "
                f"Departman: {self.__departman}, "
                f"Maaş: {self.__maas}")

    # Bilgileri göster
    def bilgileri_goster(self):
        print(self.__str__())
