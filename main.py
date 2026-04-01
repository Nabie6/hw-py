from student import Student
import file_manager

def main():
    while True:
        print("\n1. Добавить студента\n2. Просмотреть всех\n3. Удалить по ID\n4. Выход")
        choice = input("Выбор: ")
        
        if choice == "1":
            sid = input("ID: ")
            name = input("Имя: ")
            age = input("Возраст: ")
            grade = input("Оценка: ")
            email = input("Email: ")
            
            new_s = Student(sid, name, age, grade, email)
            file_manager.save_student(new_s)
            print("Сохранено!")
            
        elif choice == "2":
            data = file_manager.read_students()
            for row in data:
                print(" | ".join(row))
                
        elif choice == "3":
            sid = input("Введите ID для удаления: ")
            file_manager.delete_student(sid)
            print("Удаление завершено.")
            
        elif choice == "4":
            break

if __name__ == "__main__":
    main()