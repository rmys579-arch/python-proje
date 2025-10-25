
import os # dosyayı silmemiz yeniden adlandıramız veya sınıflandırmamız için 
import shutil # dosyaları taşımak için 
# sınıflandırma (sözlük) partı
tipler = {   
    "Belge": [ ".pdf" , ".docx" , ".txt" , ],   
    "Görsel": [ ".jpg", ".jpeg", ".gif"   ],
    "Sunum" : [ ".pptx" , ".ppt", ".key",  ]

}

#Dosyanın tipini bulalım
def dosyanın_tipi (uzantı):
 "" # dosyanın ismini küçük harfe çevir !!!!!!! .pdf ve .PDF in  aynı tipte olması için yapıyoruz
 uzantı = uzantı.lower() 
 for tip_adı , uzantılar in tipler.items():
  if uzantı in uzantılar:
   return tip_adı
  else:
   return "diğer"
  

# verilecek dizin ( dosyaların bulunduğu yer)deki dosyaları uzatılarına göre klasörleyelim
# kullanacağım fonksiyonlar =     os.path.join() bu fonksiyon verilen klasör 
# adresi ile dosyanın adını birleştiriyor 
# ve tek tam adres oluşturur.
def dosyaları_sınıflandır (dizin_adresi):
  for dosya_adı in os.list(dizin_adresi):
    "" # ögelerin adlarını döngü ile listelemiş oldum ......
    alınacak_adres = os.path.join(dizin_adresi, dosya_)
    #alınanın dosya olduğundan emin olmak için     ... buray silebiliriz de ?
    if os.path.isfile(alınacak_adres):
     # aşağıda dosyanın ismini ve uzantısınnı ayırıyoruz 
     isim, uzantı = os.path.splitext(dosya_adı)
     tip_adı = dosyanın_tipi(uzantı)
     alınacak_adres = os.path.join(dizin_adresi, tip_adı)

     # atanacak hedef bir klasor olmdığı için  klasör oluşturma kısmı
     # kullanılacak fonksiyonlar = os.make.dirs() klasor oluşturuyo
     # hedef klasör yok başta kontrol edip sonra oluşturuyorum.
     if not os.path.exists(alınacak_adres):
      os.makedirs(alınacak_adres)
     else:
      os.makedirs(alınacak_adres)
      
      
    # dosyaların bulunduğu yeri ayırıp klasörlemiş oldum. Şimdi taşıma kısmında kullanılacak fonksiyonlar
    #shutil.move(nereden alınacağı ,nereye gideceği ) alınan dosyayı başka bir yere taşıyor.
  #taşınıp taşınmama durumunda bilgi vermek için try except kullanıp sonra printliyoruz 
     
 
 
     try: 
    
       shutil.move(alınacak_adres,hedef_yol)
       print ("Taşıma işlemi gerçekleştirilmiştir." , "dosya_adı" , " ,"  ,  "tip_adı", "klasörüne taşındı. " )
     except:
      print("HATA!!!")
      