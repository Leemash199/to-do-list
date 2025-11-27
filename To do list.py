class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task}' removed!")
        except IndexError:
            print("Invalid task number!")

    def main():
      todo = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_number = int(input("Enter task number to remove: "))
            todo.remove_task(task_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

        if __name__ == "__main__":
           main()
