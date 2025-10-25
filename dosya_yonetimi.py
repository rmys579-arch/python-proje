
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
 for tip_adı , uzantılar in uzantı:
  if uzantı in uzantılar:
   return tip_adı
  else:
   return "diğer"
  
