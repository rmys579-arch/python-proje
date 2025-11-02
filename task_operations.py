
# Tarih işlemleri için datetime modülünü içeri aktarıyorum
from datetime import datetime
from file_management import find_file_type

# Dosyaya kaydetme işlevi 'dosya_yonetimi'nden geliyordu, onu da import ediyorum.
# (Burada varsayımsal olarak görevleri_kaydet fonksiyonunun dosya_yonetimi.py'de olduğunu kabul ettim)
try:
    from file_management import classify_files
except ImportError:
    # Eğer bu import hata verirse, main.py'nin kaydetme işlemini yapmasını bekleyeceğiz.
    # Ancak stabilite için burada olması daha iyi.
    print("WARNING: Could not load save_tasks function from dosya_yonetimi. Saving must be done in main.py.")
    # Bu durumda, gorev_ekle fonksiyonunun sonunda kaydetme işlemini yapmayız.

def add_tasks(current_tasks):
    """
    Kullanıcıdan yeni bir görevin detaylarını alarak (isim, son tarih, öncelik)
    mevcut görevler listesine ekler ve dosyaya kaydeder.
    """
    print("\n--- ADD A NEW TASK ---")
    
    # 1. Görev Adını 
    while True:
        task_name = input("ENTER TASK NAME (*): ").strip()
        if task_name:
            break
        print("TASK NAME CANNOT BE EMPTY. PLEASE TRY AGAIN.")
        
    # 2. Son Teslim Tarihini 
    due_date_str = input("ENTER DUE DATE (YYYY-MM-DD, Optional): ").strip()
    
    # Tarih formatını kontrol etme 
    if due_date_str:
        try:
            datetime.strptime(due_date_str, "YY-mm-dd")
        except ValueError:
            print("WARNING: INVALID DATE FORMAT. TASK WILL BE ADDED WITHOUT A DUE DATE.")
            due_date_str = None # Geçersizse None yapıyorum
        else:
            # Eğer tarih doğruysa, onu kullanmak için hazır bıraktım
            pass
    else:
        due_date_str = None # Eğer boş bırakılırsa None yapıyorum
            
    # 3. Önceliği Alıyorum
    priority_options = ["High", "Medium", "Low"]
    priority = "Medium" # Varsayılan olarak 'Orta' belirliyorum
    
    print(f"CHOOSE PRIORITY ({'/'.join(priority_options)}): ")
    while True:
        choice = input("YOUR CHOICE (Default is Orta): ").strip().capitalize()
        
        if choice in priority_options:
            priority = choice
            break
        elif not choice:
            # Kullanıcı boş bırakırsa, varsayılan 'Orta' kalır ve döngüden çıkar
            break
        else:
            print("INVALID PRIORITY CHOICE. PLEASE SELECT FROM THE LIST.")

    # 4. Yeni Görev Sözlüğünü Oluşturuyorum
    new_task = {
        "name": task_name,
        "completed": False, # Yeni görevler başlangıçta her zaman False
        "due_date": due_date_str,
        "priority": priority
    }
    
    # 5. Ana Görev Listesine Ekliyorum
    if isinstance(current_tasks, list):
        current_tasks.append(new_task)
    else:
        current_tasks = [new_task]
    
    # 6. Değişiklikleri JSON dosyasına kaydediyorum
    try:
        completed_task(current_tasks) 
        print(f"\n✅ TASK SUCCESSFULLY ADDED: '{task_name}' (Priority: {priority})")
    except NameError:
        # Eğer görevleri_kaydet import edilemediyse veya main.py'de çağrılacaksa kullanıcıyı bilgilendiriyorum.
        print(f"\n✅ TASK SUCCESSFULLY ADDED: '{task_name}' (Priority: {priority})")
        print("NOTE: Kaydetme işlemi bir sonraki adımda (main.py'de) yapılmalıdır.")

    print("-" * 30)
from file_management import completed_task

def completed_task(tasks):
    if not tasks:
        print("There are no missions.")
        return
    try:
        no = int(input("Number of completed task: "))
        # Girilen sayı görev numaraları arasında mı?
        if 1 <= no <= len(tasks):
            tasks[no - 1]["completed"] = True
            completed_task(tasks)
            print("Mission completed ✅")
        else:
            print(" Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def automatic_clean_up(tasks):
    new_list = []
    for g in tasks:
        if g["completed"] == False: #tamamlanmayan görevleri yeni listeye ekler
            new_list.append(g)
    
    tasks[:] = new_list #Eski listeyi yenisiyle değiştirir
    completed_task(tasks)
    print("completed tasks deleted")
#görevi tamamla/otomatik temizlik



def show_the_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
        return
    print("\n ---CURRENT TASKS---")
    for i, g in  enumerate(tasks,start=1):
        situation="✅"  if g [ "completed"]else "❌"
        due_date=g.get("due_date", "no date") #son_tarih yoksa no date yazdırır
        priority=g.get("priority", "priority not set") #öncelik yoksa priority no set yazdırır
        print (f"{i} - {g["Name"]} | Due : {due_date} | Priority:{priority} | Status:{situation}")
        
            