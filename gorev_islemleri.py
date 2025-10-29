
# Tarih işlemleri için datetime modülünü içeri aktarıyorum
from datetime import datetime
from dosya_yonetimi import dosyanın_tipini_bul

# Dosyaya kaydetme işlevi 'dosya_yonetimi'nden geliyordu, onu da import ediyorum.
# (Burada varsayımsal olarak görevleri_kaydet fonksiyonunun dosya_yonetimi.py'de olduğunu kabul ettim)
try:
    from dosya_yonetimi import görevleri_kaydet
except ImportError:
    # Eğer bu import hata verirse, main.py'nin kaydetme işlemini yapmasını bekleyeceğiz.
    # Ancak stabilite için burada olması daha iyi.
    print("UYARI: görevleri_kaydet fonksiyonu dosya_yonetimi'nden yüklenemedi. Kaydetme main.py'de yapılmalıdır.")
    # Bu durumda, gorev_ekle fonksiyonunun sonunda kaydetme işlemini yapmayız.

def gorev_ekle(mevcut_gorevler):
    """
    Kullanıcıdan yeni bir görevin detaylarını alarak (isim, son tarih, öncelik)
    mevcut görevler listesine ekler ve dosyaya kaydeder.
    """
    print("\n--- ADD A NEW TASK ---")
    
    # 1. Görev Adını 
    while True:
        gorev_adi = input("ENTER TASK NAME (*): ").strip()
        if gorev_adi:
            break
        print("TASK NAME CANNOT BE EMPTY. PLEASE TRY AGAIN.")
        
    # 2. Son Teslim Tarihini 
    son_tarih_str = input("ENTER DUE DATE (YYYY-MM-DD, Optional): ").strip()
    
    # Tarih formatını kontrol etme 
    if son_tarih_str:
        try:
            datetime.strptime(son_tarih_str, "%Y-%m-%d")
        except ValueError:
            print("WARNING: INVALID DATE FORMAT. TASK WILL BE ADDED WITHOUT A DUE DATE.")
            son_tarih_str = None # Geçersizse None yapıyorum
        else:
            # Eğer tarih doğruysa, onu kullanmak için hazır bıraktım
            pass
    else:
        son_tarih_str = None # Eğer boş bırakılırsa None yapıyorum
            
    # 3. Önceliği Alıyorum
    oncelik_secenekleri = ["Yüksek", "Orta", "Düşük"]
    oncelik = "Orta" # Varsayılan olarak 'Orta' belirliyorum
    
    print(f"CHOOSE PRIORITY ({'/'.join(oncelik_secenekleri)}): ")
    while True:
        secim = input("YOUR CHOICE (Default is Orta): ").strip().capitalize()
        
        if secim in oncelik_secenekleri:
            oncelik = secim
            break
        elif not secim:
            # Kullanıcı boş bırakırsa, varsayılan 'Orta' kalır ve döngüden çıkar
            break
        else:
            print("INVALID PRIORITY CHOICE. PLEASE SELECT FROM THE LIST.")

    # 4. Yeni Görev Sözlüğünü Oluşturuyorum
    yeni_gorev = {
        "isim": gorev_adi,
        "tamamlandı": False, # Yeni görevler başlangıçta her zaman False
        "son_tarih": son_tarih_str,
        "öncelik": oncelik
    }
    
    # 5. Ana Görev Listesine Ekliyorum
    if isinstance(mevcut_gorevler, list):
        mevcut_gorevler.append(yeni_gorev)
    else:
        mevcut_gorevler = [yeni_gorev]
    
    # 6. Değişiklikleri JSON dosyasına kaydediyorum
    try:
        görevleri_kaydet(mevcut_gorevler) 
        print(f"\n✅ TASK SUCCESSFULLY ADDED: '{gorev_adi}' (Priority: {oncelik})")
    except NameError:
        # Eğer görevleri_kaydet import edilemediyse veya main.py'de çağrılacaksa kullanıcıyı bilgilendiriyorum.
        print(f"\n✅ TASK SUCCESSFULLY ADDED: '{gorev_adi}' (Priority: {oncelik})")
        print("NOTE: Kaydetme işlemi bir sonraki adımda (main.py'de) yapılmalıdır.")

    print("-" * 30)
from dosya_yonetimi import görevleri_kaydet

def gorevi_tamamla(gorevler):
    if not gorevler:
        print("Hiç görev yok.")
        return
    try:
        no = int(input("Tamamlanan görevin numarası: "))
        # Girilen sayı görev numaraları arasında mı?
        if 1 <= no <= len(gorevler):
            gorevler[no - 1]["tamamlandı"] = True
            görevleri_kaydet(gorevler)
            print("Görev tamamlandı ✅")
        else:
            print("Geçersiz numara!")
    except ValueError:
        print("Lütfen bir sayı girin!")
def otomatik_temizlik(gorevler):
    yeni_liste = []
    for g in gorevler:
        if g["tamamlandı"] == False: #tamamlanmayan görevleri yeni listeye ekler
            yeni_liste.append(g)
    
    gorevler[:] = yeni_liste #Eski listeyi yenisiyle değiştirir
    görevleri_kaydet(gorevler)
    print("Tamamlanan görevler silindi")
#görevi tamamla/otomatik temizlik



def gorevleri_goster(gorevler):
    if not gorevler:
        print("görev listesi boş.")
        return
    print("\n ---CURRENT TASKS---")
    for i, g in  enumerate(gorevler,start=1):
        durum="✅"  if g [ "tamamlandı"]else "❌"
        son_tarih=g.get("son_tarih", "no date") #son_tarih yoksa no date yazdırır
        oncelik=g.get("öncelik", "priority not set") #öncelik yoksa priority no set yazdırır
        print (f"{i} - {g["isim"]} | Due : {son_tarih} | priority:{oncelik} | Status:{durum}")
        
            