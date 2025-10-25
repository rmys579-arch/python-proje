from dosya_yonetimi import dosyaları_sınıflandır
from gorev_islemleri import (
  gorevleri_goster,
  gorev_ekle,
  gorevi_tamamla,
  otomatik_temizlik  
)
def main_menu():
    print("MAİN MENU")
    print("1.SHOW THE TASKS")
    print("2.ADD A TASK")
    print("3.COMPLETE A TASK")
    print("4.AUTOMATİC CLEAN UP ")
    print("5.EXIT")
    return input( "please chose an option (1-5):") # return'den gelen cevabı fonksyona gönderip bir görev seçeceğiz
def main():
    """ ana program akışını belirleyeceğiz
    diğer modüllerden aktarılan fonksyonları birleştireceğiz
    """
    mevcut_gorevler= dosyaları_sınıflandır()
    while True:
        choose = main_menu()
        if choose =="1":
            # Kişi 2'nin 'gorevleri_goster' fonksiyonunu çağırır.
            # Görevlerin güncel halini ona parametre olarak verir.
            gorevleri_goster(mevcut_gorevler)
        elif choose=="2":
            new_task=input("PLEASE ENTER THE TASK YOU WANT TO ADD:")
            gorev_ekle(mevcut_gorevler, new_task)
        elif choose=="3":
            gorevi_tamamla(mevcut_gorevler)
        elif choose=="4":
            mevcut_gorevler=otomatik_temizlik(mevcut_gorevler)
        elif choose=="5":
            print("EXİTİNG THE PROGRAM...")
            BREAK 
        else:
            print("INVALID CHOİCE , PLEASE TRY AGAIN")
if __name__ == "__main__":
    main()
