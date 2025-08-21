task = []

if __name__ == "__main__": 
    # create a task 
    print("Creating a task... Use the task list to manage it.") 
    while True: 
        print('\n')
        print("Current tasks:", task) 
        print("Enter a task to add it to the list (or type 'exit' to quit):")
        user_input = input() 
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks") 
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if (choice == '1'):
            task_name = input("Enter the task name: ")
            task.append(task_name)
            print(f"Task '{task_name}' added.") 
            if (choice == '2'):
                task_name = input("Enter the task name to remove: ")
                if task_name in task:
                    task.remove(task_name)
                    print(f"Task '{task_name}' removed.")
                else:
                    print(f"Task '{task_name}' not found.") 
        elif (choice == '2'):
            task_name = input("Enter the task name to remove: ")
            if task_name in task:
                task.remove(task_name)
                print(f"Task '{task_name}' removed.")
            else:
                print(f"Task '{task_name}' not found.") 
        elif (choice == '3'):
            print("Current tasks:", task) 
        elif (choice == '4'):
            print("Exiting the task manager. Goodbye!")
            break  
        