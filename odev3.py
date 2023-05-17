#Magaza sinifi oluştur.
class Magaza:
    #initializer metodlu fonksiyonda private değişken tanımla ve satislar sozlugu olusturduk.
    def __init__(self, magaza_adi, satici_adi, satici_turu):
        self.magaza_adi = magaza_adi
        self.satici_adi = satici_adi
        self.satici_turu = satici_turu
        self.satislar = {}
    #Magaza adi ozelligini degistirmek icin bir metod tanimla.
    def set_magaza_adi(self, magaza_adi):
        self.magaza_adi = magaza_adi
    #Satici adini degistirmek icin bir metod tanimla.
    def set_satici_adi(self, satici_adi):
        self.satici_adi = satici_adi
    #Satici turunu degistirmek icin bir metod tanimla.
    def set_satici_turu(self, satici_turu):
        self.satici_turu = satici_turu
    #saticinin yaptigi satisları hesaplamak icin bir metod tanımla.
    def add_satis(self, miktar):
        #Eger satici adi satislar sozlugunde yoksa satisları 0'a esitle.
        if self.satici_adi not in self.satislar:
            self.satislar[self.satici_adi] = 0
        ##Varsa miktari artir.
        self.satislar[self.satici_adi] += miktar
    #Magazanin yaptigi satislari hesaplamak icin bir metod tanimla.
    def get_magaza_satis(self):
        #Toplam satisi satislar sozlugundeki degerlerin toplamina esitle.
        toplam_satis = sum(self.satislar.values())
        return toplam_satis
    #Sınıfın satislar ozelligindeki satici adi anahtarina karsilik gelen degeri dondur.
    #Eğer boyle bir anahtar yoksa varsayilan deger olarak 0 dondurur.
    def get_satici_satis(self):
        return self.satislar.get(self.satici_adi, 0)
    #Magazanın toplam satis degerini yazdirmak icin str metosu olustur ve ekrana yazdir.
    def __str__(self):
        return f"{self.magaza_adi} mağazasının toplam satışı: {self.get_magaza_satis()} TL"

#Magazalar ve satici toplam satis sozlukleri tanimla.
magazalar = {}
satici_toplam_satis = {}

def main():
    while True:
        #Kullanicidan magaza adi girdisi al.
        magaza_adi = input("Mağaza adını girin (çıkmak için q ): ")
        #Eger q girilirse donguyu sonlandir.
        if magaza_adi == "q":
            break
        #Kuulanicidan satici adi, satici turu ve satis miktarini al.
        satici_adi = input("Satıcının adını giriniz: ")
        satici_turu = input("Satıcının türünü giriniz: ")
        miktar = float(input("Satış miktarını giriniz: "))
        #Magazalar sozlugu icinde magaza anahtarini ara.
        #Eger magaza adi anahtari mevcutsa degeri magaza degiskenine ata.
        if magaza_adi in magazalar:
            magaza = magazalar[magaza_adi]
        #Degilse bir magaza nesnesi olustur ve bu nesne magaza adi anahtari ile birlikte sozluge kaydedilir.
        else:
            magaza = Magaza(magaza_adi, satici_adi, satici_turu)
            magazalar[magaza_adi] = magaza
        #Magazada satilan urunlerin hangi satici tarafindan satildigini belirle.
        magaza.set_satici_adi(satici_adi)
        #Farkli satici turlerine gore satis verilerini topla.
        magaza.set_satici_turu(satici_turu)
        #Magaza nesnesi icin add_satis metodunu cagirir ve miktar adli parametreye bir satis miktari ekler.
        magaza.add_satis(miktar)
        #Magaza nesnesinin satici adina karsilik gelen satis miktarini satis miktari degiskeninde depola.
        satis_miktari = magaza.get_satici_satis()
        #Eger satici adi adli bir sstici daha once satici toplam satis sozlugunde tanımlanmamıssa satici toplam satis
        #sozlugune satici adi adli bir anahtar 0 degerini atar.
        if satici_adi not in satici_toplam_satis:
            satici_toplam_satis[satici_adi] = 0
        #satis miktarini saticinin toplam satis miktarina ekle.
        satici_toplam_satis[satici_adi] += satis_miktari
    #Magazalar sozlugu icindeki magaza nesnelerini ekrana yazdir.
    for magaza_adi, magaza in magazalar.items():
        print(magaza)
    #Ekrana saticinin adi - toplam satis miktari basligini at.
    print("Satıcının adı - Toplam satış miktarı")
    #Satici toplam satis sozlugundeki her bir anahtar deger cifti icin bir tuple dondurur.
    #Satici adi adli degiskene anahtar, satis miktari adli degiskene de deger atanir.
    for satici_adi, satis_miktari in satici_toplam_satis.items():
        #Her bir satici adi ve satis miktarini ekrana yazdir.
        print(f"{satici_adi} - {satis_miktari} TL'dir.")
#Main metodunu cagir.
if __name__ == '__main__':
    main()
