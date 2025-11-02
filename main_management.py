from file_management import classify_files 
from task_operations import (
  add_tasks, 
  show_the_tasks,
  completed_task,
  automatic_clean_up
)
def main_menu():
    print("MAİN MENU")
    print("1.SHOW THE TASKS")
    print("2.ADD A TASK")
    print("3.COMPLETE A TASK")
    print("4.AUTOMATİC CLEAN UP ")
    print("5.EXIT")
    return input( "please choose an option (1-5):") # return'den gelen cevabı fonksiyona gönderip bir görev seçeceğiz
def main():
    """ ana program akışını belirleyeceğiz
    diğer modüllerden aktarılan fonksiyonları birleştireceğiz
    """
    current_tasks = classify_files()
    while True:
        choose = main_menu()
        if choose =="1":
            # Kişi 2'nin 'gorevleri_goster' fonksiyonunu çağırır.
            # Görevlerin güncel halini ona parametre olarak verir.
            show_the_tasks(current_tasks)
        elif choose=="2":
            add_tasks(current_tasks)
        elif choose=="3":
            completed_task(current_tasks)
        elif choose=="4":
            current_tasks=automatic_clean_up(current_tasks)
        elif choose=="5":
            print("EXİTİNG THE PROGRAM...")
            break
        else:
            print("INVALID CHOİCE , PLEASE TRY AGAIN")
if __name__ == "__main__":
    main()
