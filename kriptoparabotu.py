import ccxt 
import socket
from tkinter import *
from tkinter import messagebox
import datetime

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
ip_adress=get_ip()

lisans_bilgisi="DENEME" #lisans kodu
tarih_bilgisi=datetime.datetime(3020,12,30,12,12) #kullanım süresi
kullanici_ip=ip_adress #isterseniz kendi ip adresinizi girebilirsiniz
simdiki_tarih=datetime.datetime.now()

def ana_menu() :
        simdiki_tarih=datetime.datetime.now()
        while tarih_bilgisi > simdiki_tarih :
            simdiki_tarih=datetime.datetime.now()
            pencere = Tk()
            pencere.title(f"Kripto Para Botu.Uygulamayı {tarih_bilgisi} Kadar Kullanabilirsiniz. ")
            pencere.geometry("1500x1200")

            label=Label(pencere)
            label.config(text="Geliştirici Bilgileri",bg="cyan",font=("Arial",13))
            label.place(x=20,y=200)

            label=Label(pencere)
            label.config(text="KEREM YAĞAN",font=("Arial",13))
            label.place(x=20,y=230)

            label=Label(pencere)
            label.config(text="İletişim E-Posta:keremyagan5@gmail.com",font=("Arial",13))
            label.place(x=20,y=250)

            label=Label(pencere)
            label.config(text="Binance Referans Kimliği:59067923",font=("Arial",13))
            label.place(x=20,y=275)

            label=Label(pencere)
            label.config(text="Yeni Lisans Kodu Almak İçin Lütfen İletişime Geçiniz.",font=("Arial",13))
            label.place(x=20,y=300)

            label=Label(pencere)
            label.config(text="Banka Hesap Bilgileri",bg="yellow",font=("Arial",13))
            label.place(x=20,y=330)

            label=Label(pencere)
            label.config(text="Hesap Adı:Kerem YAĞAN",font=("Arial",13))
            label.place(x=20,y=360)

            label=Label(pencere)
            label.config(text="Banka:Ziraat Bankası",font=("Arial",13))
            label.place(x=20,y=380)

            label=Label(pencere)
            label.config(text="IBAN:TR32 0001 0003 2062 3006 2550 01",font=("Arial",13))
            label.place(x=20,y=400)

            label=Label(pencere)
            label.config(text="İşlem Yapacağınız Coinleri (XRP/TRY,BTC/BNB) Şeklinde Giriniz:",font=("Arial",10))
            label.place(x=20,y=20)
            coin_ciftler=Entry(pencere)
            coin_ciftler.place(x=450,y=20)

            label=Label(pencere)
            label.config(text="Alış Fiyat Oranı(1.05=%5fazlasına kadar alım):",font=("Arial",10))
            label.place(x=20,y=40)
            alis_oran=Entry(pencere)
            alis_oran.place(x=450,y=40)

            label=Label(pencere)
            label.config(text="Kâr Oranını Giriniz(1.07=%7kâr):",font=("Arial",10))
            label.place(x=20,y=60)
            kar_oran=Entry(pencere)
            kar_oran.place(x=450,y=60)

            label=Label(pencere)
            label.config(text="Zarar Oranını Giriniz(0.90=%10zarar):",font=("Arial",10))
            label.place(x=20,y=80)
            zarar_oran=Entry(pencere)
            zarar_oran.place(x=450,y=80)

            label=Label(pencere)
            label.config(text="Kullanılacak Para Miktarı(Hesaptaki Paranın Tamamı İçin 0 Yazınız):",font=("Arial",10))
            label.place(x=20,y=100)
            para_miktari=Entry(pencere)
            para_miktari.place(x=450,y=100)

            label=Label(pencere)
            label.config(text="Hesap Zarar Durdurma Oranı(0.95=%5zarar durdurma):",font=("Arial",10))
            label.place(x=20,y=120)
            hesap_zarar=Entry(pencere)
            hesap_zarar.place(x=450,y=120)

            label=Label(pencere)
            label.config(text="Hesap Kâr Oranı Giriniz:",font=("Arial",10))
            label.place(x=20,y=140)
            hesap_kar_orani_1=Entry(pencere)
            hesap_kar_orani_1.place(x=450,y=140)

            label=Label(pencere)
            label.config(text="Api Bilginizi Giriniz:",font=("Arial",10))
            label.place(x=20,y=160)
            api_key=Entry(pencere)
            api_key.place(x=450,y=160)

            label=Label(pencere)
            label.config(text="Secret Api Bilgisini Giriniz:",font=("Arial",10))
            label.place(x=20,y=180)
            secret_api=Entry(pencere)
            secret_api.place(x=450,y=180)

            liste=[]
            def bilgiler():
                liste.append(coin_ciftler.get())
                liste.append(alis_oran.get())
                liste.append(kar_oran.get())
                liste.append(zarar_oran.get())
                liste.append(para_miktari.get())
                liste.append(hesap_zarar.get())
                liste.append(api_key.get())
                liste.append(secret_api.get())
                liste.append(hesap_kar_orani_1.get())
                
                
            simdiki_tarih=datetime.datetime.now()
            buton=Button(pencere)
            buton.config(text="Onayla",bg="black",fg="white",command=bilgiler)
            buton.place(x=450,y=200)
            pencere.mainloop()
            simdiki_tarih=datetime.datetime.now()

            alinabliecek_coin_ciftleri=liste[0].split(",")
            alis_fiyat_orani=1+(float(liste[1])/100)
            kar_satis_orani=(float(liste[2])/100)+1
            zararina_satis_orani=1-(float(liste[3])/100)
            kullanilacak_para=float(liste[4])
            hesaptaki_zarar_orani=1-(float(liste[5])/100)
            api=liste[6]
            secret_api=liste[7]
            hesap_kar_orani=1+(float(liste[8])/100)
            simdiki_tarih=datetime.datetime.now()

            import time
            import ccxt 
            exchange_id = "binance"
            exchange_class = getattr(ccxt, exchange_id)
            exchange = exchange_class({
                'apiKey': api, 
                'secret': secret_api,
                'timeout': 30000,
                'enableRateLimit': True,})            
            while tarih_bilgisi > simdiki_tarih :
                alinmis_coin_ciftleri=[] #alınan coin çiftleri bu listeye eklenir,sistem bunu otomatik yapar
                alinabliecek_coin_ciftleri_copy=alinabliecek_coin_ciftleri.copy()
                for coinler in alinabliecek_coin_ciftleri_copy :
                    coin_name=coinler.split("/")[0]
                    coin_cifti=coinler.split("/")[1]
                    while True :
                        try :
                            son_siparis_dict=exchange.fetchClosedOrders(coin_name+"/"+coin_cifti)
                            break
                        except Exception :
                            pass
                    son_siparis=dict(list(son_siparis_dict)[-1]) #ilgili coine ait son işlem bilgileri alınıyor
                    son_islem_adi=son_siparis["info"]["side"]
                    if son_islem_adi == "BUY" :
                        alinmis_coin_ciftleri.append(coinler)
                        alinabliecek_coin_ciftleri.remove(coinler)

                stop_artis=[]  # stop satıştaki artış kısmı,sistem kendisi kullanıyor bu bölümü
                zirve_artis=[] # zirve satıştaki artış kısmı,sistem kendisi kullanıyor bu bölümü
                for oran in alinabliecek_coin_ciftleri_copy :
                    stop_artis.append("0") #stop artış değeri 0 olarak başlar
                    zirve_artis.append("0") #zirve artış değeri 0 olarak başlar



                while True :
                    try :
                        exchange_account_balance=exchange.fetchBalance()
                        break
                    except Exception :
                        pass
                account_balance=float(exchange_account_balance[alinabliecek_coin_ciftleri_copy[0].split("/")[1]]["free"])

                toplam_deger=0
                son_deger=0
                for coinler in alinabliecek_coin_ciftleri :
                    coin_name=coinler.split("/")[0]
                    coin_cifti=coinler.split("/")[1]                    
                    while True :
                        try :
                            exchange_account_balance=exchange.fetchBalance()
                            break
                        except Exception :
                            pass
                    balance_coin=float((exchange_account_balance[coin_name]["free"]))
                    while True :
                        try :
                            fiyatlar=exchange.fetch_ticker(coin_name+"/"+coin_cifti)
                            break
                        except Exception:
                            pass
                    anlik_kur=float(fiyatlar["info"]["lastPrice"])
                    toplam_deger=toplam_deger+(balance_coin*anlik_kur)

                while True :
                    try :
                        exchange_account_balance=exchange.fetchBalance()
                        break
                    except Exception :
                        pass
                account_balance=float(exchange_account_balance[alinabliecek_coin_ciftleri_copy[0].split("/")[1]]["free"])    
                toplam_deger=toplam_deger+account_balance
                kosul=toplam_deger*hesap_kar_orani>son_deger
                while kosul :
                    son_deger=0
                    for coinler in alinabliecek_coin_ciftleri_copy :
                        coin_name=coinler.split("/")[0]
                        coin_cifti=coinler.split("/")[1]                        
                        while True :
                            try :
                                exchange_account_balance=exchange.fetchBalance()
                                break
                            except Exception :
                                pass
                        balance_coin=float((exchange_account_balance[coin_name]["free"]))
                        while True :
                            try :
                                fiyatlar=exchange.fetch_ticker(coin_name+"/"+coin_cifti)
                                break
                            except Exception:
                                pass
                        anlik_kur=float(fiyatlar["info"]["lastPrice"])
                        son_deger=son_deger+(balance_coin*anlik_kur)

                    while True :
                        try :
                            exchange_account_balance=exchange.fetchBalance()
                            break
                        except Exception :
                            pass
                    account_balance=float(exchange_account_balance[alinabliecek_coin_ciftleri_copy[0].split("/")[1]]["free"])     
                    son_deger=son_deger+account_balance
                    if not len(alinabliecek_coin_ciftleri) == 0 :
                        for coinler in alinabliecek_coin_ciftleri : #seçilen coinlerden şarta uygun olanlarının alım işlemi gerçekleşiyor
                            #bot çalışır çalışmaz yapacağı ilk işlem seçilen coinlerden uygun şarttakileri satın almak olacaktır
                            coin_name=coinler.split("/")[0]
                            coin_cifti=coinler.split("/")[1]
                            while True :
                                try :
                                    exchange_account_balance=exchange.fetchBalance()
                                    break
                                except Exception :
                                    pass
                            account_balance=float(exchange_account_balance[alinabliecek_coin_ciftleri_copy[0].split("/")[1]]["free"])
                            
                            while True :
                                try :
                                    fiyatlar=exchange.fetch_ticker(coin_name+"/"+coin_cifti)
                                    break
                                except Exception as err:
                                    pass
                            anlik_kur=float(fiyatlar["info"]["lastPrice"])

                            time.sleep (exchange.rateLimit / 1000) # time.sleep wants seconds
                            while True :
                                try :
                                    liste=(coin_name+"/"+coin_cifti, exchange.fetch_ohlcv (coin_name+"/"+coin_cifti,'30m')) # thirty minutes
                                    break
                                except Exception as err:
                                    pass
                                
                            asil_liste=liste[1]
                            asil_liste.reverse()
                            fiyat_liste=asil_liste[:1]

                            for i in fiyat_liste :
                                en_yuksek=i[2]
                                en_dusuk=i[3]

                            alinacak_fiyat=en_dusuk*alis_fiyat_orani #alınacak fiyat hesaplanır
                            if (anlik_kur < alinacak_fiyat) or (anlik_kur == alinacak_fiyat) :
                                alim_oran = 100
                                if (account_balance == 10) or (account_balance > 10) :
                                    while True : 
                                        try :
                                            if alim_oran > 70 :
                                                alim_miktari=(account_balance/anlik_kur/len(alinabliecek_coin_ciftleri))*(89.8+(alim_oran*0.1))/100 #paranın tamamı ile alamıyoruz komisyon kesintisi sebebi ile
                                                market_alis=exchange.create_market_buy_order(coin_name+'/'+coin_cifti,alim_miktari) #alış işlemi yapılıyor
                                                alinmis_coin_ciftleri.append(coinler) #alınan coin adları listeye ekleniyor
                                                alinabliecek_coin_ciftleri.remove(coinler) #alınan coin adını alınabilecekler listesinden çıkarıyor
                                                print(f"Alınan Coin:{coin_name} Alınan Miktar:{round(alim_miktari,4)} Ödenen Tutar:{round(anlik_kur*alim_miktari,4)}".format(coin_name,round(alim_miktari,4),round(anlik_kur*alim_miktari,4)))
                                                break 
                                            else :
                                                break
                                        except:
                                            alim_oran=alim_oran-1

                            else :
                                print(f"Satın Alma Bekleniyor.Coin Adı:{coin_name} Anlık Kur:{anlik_kur} Hedeflenen Fiyat:{alinacak_fiyat} veya Daha Az.".format(coin_name,anlik_kur,alinacak_fiyat))
                
                    if not len(alinmis_coin_ciftleri) == 0 :
                        for coinler in alinmis_coin_ciftleri : #her coin için satış gerçekleşiyor mu diye kontrol yapıyor
                            coin_name=coinler.split("/")[0]
                            coin_cifti=coinler.split("/")[1]
                            while True :
                                try :
                                    exchange_account_balance=exchange.fetchBalance()
                                    break
                                except Exception :
                                    pass
                            account_balance=float(exchange_account_balance[alinabliecek_coin_ciftleri_copy[0].split("/")[1]]["free"])
                            sira=alinabliecek_coin_ciftleri_copy.index(coinler)
                            while True :
                                try :
                                    son_siparis_dict=exchange.fetchClosedOrders(coin_name+"/"+coin_cifti)
                                    break
                                except Exception as err :
                                    pass
                            son_siparis=dict(list(son_siparis_dict)[-1]) #ilgili coine ait son işlem bilgileri alınıyor
                            son_islem_adi=son_siparis["info"]["side"]
                            son_islem_fiyati=son_siparis["price"] 
                            son_islem_miktari=son_siparis["amount"]
                            while True :
                                try:
                                    exchange_account_balance=exchange.fetchBalance()
                                    break
                                except Exception as err:
                                    pass
                            hesaptaki_coin=float((exchange_account_balance[coin_name]["free"]))
                            alis_fiyati=son_islem_fiyati
                            while True :
                                try :
                                    fiyatlar=exchange.fetch_ticker(coin_name+"/"+coin_cifti)
                                    break
                                except Exception as err :
                                    pass
                            anlik_kur=float(fiyatlar["info"]["lastPrice"])
                            
                            stop_noktasi=alis_fiyati*zararina_satis_orani #en az zararla satmak için belirlenen satış noktası
                            zirve_satis=alis_fiyati*kar_satis_orani #hedeflenen kâra ulaşınca satılacak olan nokta
                            
                            if (anlik_kur > alis_fiyati)  :
                                if anlik_kur-alis_fiyati > float(stop_artis[sira]) :
                                    stop_artis[sira]=str(round(anlik_kur-alis_fiyati,5)) #stop noktası üste taşınır

                                
                            if anlik_kur > zirve_satis : #zirve satış noktası üste taşınır
                                if zirve_satis < anlik_kur*98/100 : #anlık kur ile takip mesafesi bırakılır
                                    #çünkü zirveyi geçtikten sonra biraz aşağı inip tekrar çıkabilir
                                    #aradaki fark %1 olarak belirlenmiştir
                                    zirve_artis[sira] =str(anlik_kur*98/100)
                                elif anlik_kur-zirve_satis > float(zirve_artis[sira]) :
                                    zirve_artis[sira]=str(anlik_kur-zirve_satis)
                            
                            

                            if (anlik_kur < (stop_noktasi+float(stop_artis[sira]))) and (hesaptaki_coin*anlik_kur > account_balance*hesaptaki_zarar_orani)  :
                                try :
                                    market_satis=exchange.create_market_sell_order(coin_name+'/'+coin_cifti,hesaptaki_coin)
                                    #satış işlemi                                 
                                    alinabliecek_coin_ciftleri.append(coinler) #aynı öğeyi tekrar satın alınabilir kılmak için listeye ekliyoruz
                                    zarar_miktari=round((alis_fiyati-anlik_kur)*hesaptaki_coin,4)
                                    stop_artis[sira]=0
                                    zirve_artis[sira]=0
                                    alinmis_coin_ciftleri.remove(coinler)
                                    print(f"Zararına Satış Yapıldı.Satılan Coin:{coin_name} Zarar Miktarı:{zarar_miktari} TRY".format(coin_name,zarar_miktari))

                                except Exception as err :
                                    print(f"{coin_name} Satmak İçin Minimum Miktara Sahip Değilsiniz.Satılabilir Miktar:{hesaptaki_coin}".format(coin_name,hesaptaki_coin))

                            if (anlik_kur == (zirve_satis+float(zirve_artis[sira]))) or (anlik_kur > (zirve_satis+float(zirve_artis[sira])))  :
                                try :
                                    market_satis=exchange.create_market_sell_order(coin_name+'/'+coin_cifti,hesaptaki_coin)
                                    #satış işlemi
                                    alinmis_coin_ciftleri.remove(coinler)
                                    alinabliecek_coin_ciftleri.append(coinler) #aynı öğeyi tekrar satın alınabilir kılmak için listeye ekliyoruz
                                    zirve_artis[sira]="0"
                                    stop_artis[sira]="0"
                                    kar_miktari=(anlik_kur-alis_fiyati)*hesaptaki_coin
                                    print(f"Kâr Elde Edildi.Satılan Coin:{coin_name} Kâr Miktarı:{kar_miktari} TRY".format(coin_name,kar_miktari))
        
                                except Exception as err :
                                    print(f"{coin_name} Satmak İçin Minimum Miktara Sahip Değilsiniz.Satılabilir Miktar:{hesaptaki_coin}".format(coin_name,hesaptaki_coin))

                            print(f"Satış İşlemi Bekleniyor.Coin:{coin_name} Anlık Kur:{anlik_kur} Zirve Satış:{zirve_satis+float(zirve_artis[sira])} Stop Satış:{stop_noktasi+float(stop_artis[sira])} ".format(coin_name,anlik_kur,zirve_satis+float(zirve_artis[sira]),stop_noktasi+float(stop_artis[sira])))
                            print(f"Hesabın Güncel Değeri:{son_deger}".format(son_deger))

                for coinler in alinabliecek_coin_ciftleri_copy :
                    coin_name=coinler.split("/")[0]
                    coin_cifti=coinler.split("/")[1]                    
                    while True :
                        try :
                            exchange_account_balance=exchange.fetchBalance()
                            break
                        except Exception :
                            pass

                    balance_coin=float((exchange_account_balance[coin_name]["free"]))
                    market_satis=exchange.create_market_sell_order(coin_name+'/'+coin_cifti,balance_coin)
                    print(f"{coin_name} Satıldı.".format(coin_name))

                print("İşlemler Bitti.")                
            break
            

if ip_adress == kullanici_ip : #ip bilgileri
    pencere = Tk()
    pencere.title("Lisans Onaylama")
    pencere.geometry("600x300")

    label=Label(pencere)
    label.config(text="Sistemin Çalışma Süresi Boyunca Lütfen Bilgisayarınızı Kapatmayın.",font=("Arial",13))
    label.place(x=20,y=20)

    label=Label(pencere)
    label.config(text="Lisans Kodunu Giriniz:",bg="blue",font=("Arial",10))
    label.place(x=20,y=100)
    lisans_kod=Entry(pencere)
    lisans_kod.place(x=170,y=100)
    buton=Button(pencere)

    def lisans_onaylama():
        if (lisans_kod.get() == lisans_bilgisi) and (tarih_bilgisi < simdiki_tarih) :
            label=Label(pencere)
            label.config(text="Kodun Süresi Dolmuştur.",font=("Arial",20))
            label.place(x=20,y=130)
            
        elif (lisans_kod.get() == lisans_bilgisi) and (tarih_bilgisi > simdiki_tarih) :
            pencere.destroy()
            ana_menu()

        elif not (lisans_kod.get() == lisans_bilgisi) :
            label=Label(pencere)
            label.config(text="\nGeçersiz Kod.Lütfen Tekrar Deneyiniz",font=("Arial",20))
            label.place(x=20,y=130)
            

    buton.config(text="Onayla",bg="black",fg="white",command=lisans_onaylama)
    buton.place(x=350,y=220)
    pencere.mainloop()
    

else :
    pencere = Tk()
    pencere.title(f"Kripto Para Botu")
    pencere.geometry("500x300")

    label=Label(pencere)
    label.config(text="IP Adresi Geçerli Değil.Lütfen Geliştirici İle İletişime Geçiniz.",font=("Arial",13))
    label.place(x=20,y=20)

    label=Label(pencere)
    label.config(text="Geliştirici Bilgileri",bg="cyan",font=("Arial",13))
    label.place(x=20,y=50)

    label=Label(pencere)
    label.config(text="KEREM YAĞAN",font=("Arial",13))
    label.place(x=20,y=80)

    label=Label(pencere)
    label.config(text="İletişim E-Posta:keremyagan5@gmail.com",font=("Arial",13))
    label.place(x=20,y=100)

    label=Label(pencere)
    label.config(text="Binance Referans Kimliği:59067923",font=("Arial",13))
    label.place(x=20,y=125)

    pencere.mainloop()






            





    
