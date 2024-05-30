# "pandas" kütüphanesi veri yapıları ve veri analiz araçlarını sağlar
import pandas as pd
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta
from personel import Personel

try:
    # Personel nesnelerini oluşturma
    personel1 = Personel("101", "Mehmet", "Aksoy", "Temizlik", 1500)
    personel2 = Personel("102", "Mustafa", "Kaya", "Danışman", 2000)

    # Doktor nesnelerini oluşturma
    doktor1 = Doktor("201", "Şeyma", "Kurt", "Kardiyoloji", 20000, "Beyin Cerrahisi", 3, "Ege Üniversitesi Hastanesi")
    doktor2 = Doktor("202", "Fatih", "Arslan", "Pediatri", 15000, "Endekrinoloji", 6, "Dokuz Eylül Üniversitesi Hastanesi")
    doktor3 = Doktor("203", "Hüseyin", "Çelik", "Psikiyatri", 10000, "Nöropsikiyatri", 9, "Bayraklı Hastanesi")

    # Hemşire nesnelerini oluşturma
    hemsire1 = Hemsire("301", "Nurallah", "Güzen", "Acil Servis", 7000, 40, "Acil Servis Sertifikası", "Bayraklı Hastanesi")
    hemsire2 = Hemsire("302", "Ali", "Yılmaz", "Cerrahi", 8000, 35, "Cerrahi Sertifikası", "Ege üniversitesi Hastanesi")
    hemsire3 = Hemsire("303", "Hasan", "Öztürk", "Yoğun Bakım", 5000, 38, "Yoğun Bakım Sertifikası ", "Çiğli Hastanesi")

    # Hasta nesnelerini oluşturma
    hasta1 = Hasta("1", "yusuf", "Şahin", "1992-03-05", "Yüksek Tansiyon", "İlaç Tedavisi")
    hasta2 = Hasta("2", "İsmail", "Çalışkan", "2000-10-17", "Grip", "İlaç Tedavisi")
    hasta3 = Hasta("3", "Hasan", "Doğan", "1975-01-28", "Kanser", "İlaç Tedavisi")

    # DataFrame için veri listesi oluşturma
    data = []

    # Personel bilgilerini ekleme
    for personel in [personel1, personel2]:
        data.append([personel.get_personel_no(), personel.get_ad(), personel.get_soyad(), personel.get_departman(),
                     personel.get_maas(), None, None, None, None, None, None, None, None, None])

    # Doktor bilgilerini ekleme
    for doktor in [doktor1, doktor2, doktor3]:
        data.append([doktor.get_personel_no(), doktor.get_ad(), doktor.get_soyad(), doktor.get_departman(),
                     doktor.get_maas(), doktor.get_uzmanlik(), doktor.get_deneyim_yili(), doktor.get_hastane(),
                     None, None, None, None, None, None])

    # Hemşire bilgilerini ekleme
    for hemsire in [hemsire1, hemsire2, hemsire3]:
        data.append([hemsire.get_personel_no(), hemsire.get_ad(), hemsire.get_soyad(), hemsire.get_departman(),
                     hemsire.get_maas(), None, None, hemsire.get_hastane(), hemsire.get_calisma_saati(),
                     hemsire.get_sertifika(), None, None, None, None])

    # Hasta bilgilerini ekleme
    for hasta in [hasta1, hasta2, hasta3]:
        data.append([hasta.get_hasta_no(), hasta.get_ad(), hasta.get_soyad(), None, None, None, None, None, None, None,
                     hasta.get_hasta_no(), pd.to_datetime(hasta.get_dogum_tarihi()), hasta.get_hastalik(),
                     hasta.get_tedavi()])

    # DataFrame oluşturma
    df = pd.DataFrame(data, columns=["No", "Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı",
                                     "Hastane", "Çalışma Saati", "Sertifika", "Hasta No", "Doğum Tarihi",
                                     "Hastalık", "Tedavi"])

    # Boş olan değişken değerlerine 0 atama
    df.fillna(0, inplace=True)

    # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama ve yazdırma
    doktor_grup = df[df["Uzmanlık"] != 0].groupby("Uzmanlık").size()
    print("\nDoktor Sayısı Uzmanlık Alanına Göre:")
    print(doktor_grup)

    # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
    deneyimli_doktor_sayisi = df[df["Deneyim Yılı"] > 5].shape[0]
    print("\n5 Yıldan Fazla Deneyime Sahip Doktor Sayısı:", deneyimli_doktor_sayisi)

    # Hasta adına göre DataFrame'i alfabetik olarak sıralama ve yazdırma
    df_hasta_sirali = df[df["Hasta No"] != 0].sort_values(by="Ad")
    print("\nHasta DataFrame'i (Alfabetik Sıralı):")
    print(df_hasta_sirali)

    # Maaşı 7000 TL üzerinde olan personelleri bulma ve yazdırma
    maas_ustunde_personel = df[df["Maaş"] > 7000][["No", "Ad", "Soyad", "Departman"]]
    print("\nMaaşı 7000 TL Üzerinde Olan Personeller:")
    print(maas_ustunde_personel)

    # Doğum tarihi 1990 ve sonrası olan hastaları bulma ve yazdırma
    df_dogum_1990 = df[pd.to_datetime(df["Doğum Tarihi"]) >= "1990-01-01"]
    print("\nDoğum Tarihi 1990 ve Sonrası Olan Hastalar:")
    print(df_dogum_1990)

    # Yeni DataFrame oluşturma (ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini içeren)
    yeni_df = df[["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"]]
    print("\nYeni DataFrame:")
    with pd.option_context('display.max_rows', None, 'display.max_columns',
                           None):  # Tüm satır ve sütunları göstermek için
        print(yeni_df)


except Exception as e:
    print(f"Hata oluştu: {e}")





