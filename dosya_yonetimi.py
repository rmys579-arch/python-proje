
import os # dosyayı silmemiz yeniden adlandıramız veya sınıflandırmamız için 
import shutil # dosyaları taşımak için 
import json #uygulama kapandığında verilerin kaybolmaması için gerekli!!
# sınıflandırma (sözlük) partı
tipler = {   
    "Belge": [ ".pdf" , ".docx" , ".txt" , ],   
    "Görsel": [ ".jpg", ".jpeg", ".gif"   ],
    "Sunum" : [ ".pptx" , ".ppt", ".key",  ]

}

#Dosyanın tipini bulalım
def dosyanın_tipini_bul(uzantı):
  """Dosya uzantısını küçük harfe çevirip tipini döndürür. Eğer bulunamazsa 'diğer' döner."""
  uzantı = uzantı.lower()
  for tip_adı, uzantılar in tipler.items():
    if uzantı in uzantılar:
      return tip_adı
  return "diğer"
  

# verilecek dizin ( dosyaların bulunduğu yer)deki dosyaları uzatılarına göre klasörleyelim
# kullanacağım fonksiyonlar =     os.path.join() bu fonksiyon verilen klasör 
# adresi ile dosyanın adını birleştiriyor 
# ve tek tam adres oluşturur.
def dosyaları_sınıflandır(dizin_adresi='.'):
    """Verilen dizindeki dosyaları uzantılarına göre klasörlere taşır. Varsayılan olarak çalışma dizini kullanılır."""
    for dosya_adı in os.listdir(dizin_adresi):
    # dosyanın tam yolunu oluştur
     alınacak_adres = os.path.join(dizin_adresi, dosya_adı)

    # sadece dosyalarla ilgileniyoruz
    if os.path.isfile(alınacak_adres):
      # dosya adını ve uzantısını ayır
      isim, uzantı = os.path.splitext(dosya_adı)
      tip_adı = dosyanın_tipini_bul(uzantı)
      hedef_yol = os.path.join(dizin_adresi, tip_adı)

      # hedef klasörü oluştur (yoksa)
      if not os.path.exists(hedef_yol):
        os.makedirs(hedef_yol)

      # taşıma işlemi
      try:
        shutil.move(alınacak_adres, hedef_yol)
        print("Taşıma işlemi gerçekleştirilmiştir.", dosya_adı, ",", tip_adı, "klasörüne taşındı.")
      except Exception as e:
        print("HATA!!!", e)

#görevleri yükleme partı...
görev_dosyası = "görevler.json"
def görevleri_yükle():
# uygulama ilk çalıştığında görev dosyası yok o yüzden:
  if not os.path.exists(görev_dosyası):
    print("görev dosyası yoktur.Boş liste döndürülmektedir. ")
    return []
  
# Aşağıda direkt dosyayı açma işlemini yazıcam dosya içeriği hatalı olması durumunda kontrol edebilmek için
#yine try except ile yazıyorum....

  try:
   with open(görev_dosyası,"r")as file:
    görevler=json.load(file)
    print(f"işlem başarıldı. Görevler {görev_dosyası} dosyasından yüklendi")
    return görevler
  
  except Exception :
   print("Hata!!! Boş dosya döndürülüyor.")
   return []


 # görevleri kaydetme partı burayı da hata önlemek için try except ile yazıyoruz
def görevleri_kaydet(görevler):
    try:
        with open(görev_dosyası, "w") as file:
            # json.dump() veriyi JSON formatına dönüştürür ve dosyaya yazar
            json.dump(görevler, file, ensure_ascii=False, indent=2)
        print(f"Görevler {görev_dosyası} dosyasına kaydedilmiştir...")
    except Exception as e:
        print("Hata!!!! Görevler kaydedilemedi", e)
  #####