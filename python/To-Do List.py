# Simple To-Do List
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- Your To-Do Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    view_tasks()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
