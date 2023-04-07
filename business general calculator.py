while True:
    print("1-Ürün kar hesaplama\n2-Ciro hesaplama\n3-Sistemi kapat\n")
    a = int(input("Ne yapmak istersiniz: "))

    if a == 1:
        adet = int(input("Kaç adet satıldı?: "))
        fiyat = int(input("Ürünün fiyatı ne?: "))
        maliyet = int(input("Bu üründeki toplam maliyet nedir?: "))
        kar = adet * (fiyat - maliyet)
        print("\nBu üründeki kazancınız: ", kar, "TL")

        if kar < 0:
            print("Bu üründe", abs(kar), "TL zarardasınız.\n")
        else:
            print()

    elif a == 2:
        yis = int(input("Yurtiçi satış toplamınızı giriniz: "))
        yds = int(input("Yurtdışı satış toplamlarınızı giriniz (Yurtdışı satışınız yoksa 0 yazınız): "))
        dg = int(input("Diğer gelirleri giriniz: "))
        sais = int(input("Satış iskonto toplamını giriniz: "))
        sati = int(input("Satışlardan toplam iadelerinizi giriniz: "))
        di = int(input("Diğer indirimleri ve giderleri yazınız: "))
        ciro = yis + yds + dg - sais - sati - di
        print("\nCironuz: ", ciro, "TL\n")

    elif a == 3:
        print("Sistem kapatılıyor.")
        break

    else:
        print("Lütfen geçerli bir seçim yapınız.\n")
