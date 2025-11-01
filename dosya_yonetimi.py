
import os # dosyayı silmemiz yeniden adlandıramız veya sınıflandırmamız için 
import shutil # dosyaları taşımak için 
import json #uygulama kapandığında verilerin kaybolmaması için gerekli!!
# sınıflandırma (sözlük) partı
types = {   
    "Document": [ ".pdf" , ".docx" , ".txt" , ],   
    "Image": [ ".jpg", ".jpeg", ".gif"   ],
    "Presentation" : [ ".pptx" , ".ppt", ".key",  ]

}

#Dosyanın tipini bulalım
def find_file_type(extension):
  """Dosya uzantısını küçük harfe çevirip tipini döndürür. Eğer bulunamazsa 'diğer' döner."""
  extension = extension.lower()
  for type_name, extensions in types.items():
    if extension in extensions:
      return type_name
  return "other"
  

# verilecek dizin ( dosyaların bulunduğu yer)deki dosyaları uzatılarına göre klasörleyelim
# kullanacağım fonksiyonlar =     os.path.join() bu fonksiyon verilen klasör 
# adresi ile dosyanın adını birleştiriyor 
# ve tek tam adres oluşturur.
def classify_files(directory_address='.'):
    """Verilen dizindeki dosyaları uzantılarına göre klasörlere taşır. Varsayılan olarak çalışma dizini kullanılır."""
    for file_name in os.listdir(directory_address):
        # dosyanın tam yolunu oluştur
        source_address = os.path.join(directory_address, file_name)

    # sadece dosyalarla ilgileniyoruz
    if os.path.isfile(source_address):
      # dosya adını ve uzantısını ayır
      name , extension = os.path.splitext(file_name)
      type_name = find_file_type(extension)
      target_path = os.path.join(directory_address, type_name)

      # hedef klasörü oluştur (yoksa)
      if not os.path.exists(target_path):
        os.makedirs(target_path)

      # taşıma işlemi
      try:
        shutil.move(alınacak_adres, hedef_yol)
        print("The move has been completed.", dosya_adı, ",", tip_adı, "moved to folder.")
      except Exception as e:
        print("ERROR!!!", e)

#görevleri yükleme partı...
görev_dosyası = "görevler.json"
def görevleri_yükle():
# uygulama ilk çalıştığında görev dosyası yok o yüzden:
  if not os.path.exists(görev_dosyası):
    print("There is no task file. An empty list is returned.")
    return []
  
# Aşağıda direkt dosyayı açma işlemini yazıcam dosya içeriği hatalı olması durumunda kontrol edebilmek için
#yine try except ile yazıyorum....

  try:
   with open(görev_dosyası,"r")as file:
    görevler=json.load(file)
    print(f"Operation successful. Tasks {görev_dosyası} loaded from file")
    return görevler
  
  except Exception :
   print("Error!!! Empty file is returned.")
   return []


 # görevleri kaydetme partı burayı da hata önlemek için try except ile yazıyoruz
def görevleri_kaydet(görevler):
    try:
        with open(görev_dosyası, "w") as file:
            # json.dump() veriyi JSON formatına dönüştürür ve dosyaya yazar
            json.dump(görevler, file, ensure_ascii=False, indent=2)
        print(f"Tasks {görev_dosyası} saved in file...")
    except Exception as e:
        print("Error!!!! Quests could not be saved", e)
  #####
