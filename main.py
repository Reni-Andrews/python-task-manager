from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n--- Python Task Manager ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Search Tasks")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            date = input("Enter due date (YYYY-MM-DD): ")
            tid = manager.add_task(title, date)
            print(f"Task added with ID: {tid}")

        elif choice == '2':
            if not manager.tasks:
                print("No tasks found.")
            for t in manager.tasks:
                print(f"[{t['id']}] {t['title']} - {t['status']} (Due: {t['due_date']})")

        elif choice == '3':
            try:
                tid = int(input("Enter Task ID to mark complete: "))
                if manager.mark_complete(tid):
                    print("Task updated!")
                else:
                    print("Task ID not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        elif choice == '4':
            keyword = input("Enter search keyword: ")
            results = manager.search_tasks(keyword)
            for t in results:
                print(f"[{t['id']}] {t['title']} ({t['status']})")

        elif choice == '5':
            try:
                tid = int(input("Enter Task ID to delete: "))
                if manager.delete_task(tid):
                    print("Task deleted.")
                else:
                    print("Task ID not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()