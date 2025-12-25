
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
        shutil.move(source_address, target_path)
        print("The move has been completed.", file_name , ",", type_name , "moved to folder.")
      except Exception as e:
        print("ERROR!!!", e)

    # After (optionally) classifying files, return the current task list if any.
    # This makes classify_files() usable by main_management.py which expects a task list.
    try:
        return load_tasks()
    except NameError:
        # If load_tasks is not available for some reason, return an empty list
        return []

#görevleri yükleme partı...
task_file = "tasks.json"
def load_tasks():
# uygulama ilk çalıştığında görev dosyası yok o yüzden:
  if not os.path.exists(task_file):
    print("There is no task file. An empty list is returned.")
    return []
  
# Aşağıda direkt dosyayı açma işlemini yazıcam dosya içeriği hatalı olması durumunda kontrol edebilmek için
#yine try except ile yazıyorum....

  try:
   with open(task_file,"r")as file:
    tasks=json.load(file)
    print(f"Operation successful. Tasks {task_file} loaded from file")
    return tasks
  
  except Exception :
   print("Error!!! Empty file is returned.")
   return []


 # görevleri kaydetme partı burayı da hata önlemek için try except ile yazıyoruz
def save_tasks(tasks):
    try:
        with open(task_file, "w") as file:
            # json.dump() veriyi JSON formatına dönüştürür ve dosyaya yazar
            json.dump(tasks, file, ensure_ascii=False, indent=2)
        print(f"Tasks {task_file} saved in file...")
    except Exception as e:
        print("Error!!!! Quests could not be saved", e)
  #####
