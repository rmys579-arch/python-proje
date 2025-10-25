
import os # dosyayı silmemiz yeniden adlandıramız veya sınıflandırmamız için 
import shutil # dosyaları taşımak için 
# sınıflandırma (sözlük) partı
Sınıflandırma = {   
    "Belge": [ ".pdf" , ".docx" , ".txt" , ],   
    "Görsel": [ ".jpg", ".jpeg", ".gif"   ],
    "Sunum" : [ ".pptx" , ".ppt", ".key",  ]

}

#Dosyanın tipini bulalım
def dosyanın_tipi (uzantı):