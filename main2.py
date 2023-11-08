class Task:
    def __init__(self, name, description, priority, deadline):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nPriority: {self.priority}\nDeadline: {self.deadline}\nStatus: {'Completed' if self.completed else 'Not completed'}"

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        priority = int(input("Enter task priority: "))
        deadline = input("Enter task deadline: ")
        task = Task(name, description, priority, deadline)
        self.tasks.append(task)

    def remove_task(self):
        name = input("Enter task name: ")
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                break

    def order_by_priority(self):
        self.tasks.sort(key=lambda x:x[5])
    def view_tasks(self):
        for task in self.tasks:
            print("|---------------------|")
            print(task)
            
        

    def mark_task_as_completed(self):
        name = input("Enter task name: ")
        for task in self.tasks:
            if task.name == name:
                task.mark_as_completed()
                break

manager = TodoListManager()
def main():
    while True:
       print('1. Add:')
       print('2. Remove:')
       print('3. Sort by priority:')
       print('4. Show:')
       print('5. Mark task as completed:')
       inp = input("Input your choice:")
       if inp == '1':
        manager.add_task()
       elif inp == '2':
        manager.remove_task()
       elif inp == '3':
        manager.order_by_priority()
       elif inp == '4':
        manager.view_tasks()
       elif inp == '5':
        manager.mark_task_as_completed()
       else:
          print("Invalid input")
       choice = input('Do you want to continue? (Y/N)')
       if choice.lower() != 'y':
          break
def console():

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.login(username, password)
            main()
        elif choice == '3':
            print("Exit:")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    console()

