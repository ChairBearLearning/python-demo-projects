#note - for python v 2.x input() function tries to evaluate the inputted value before returning,
#so when you have an input value it tries to find the variable/name causing the issue. ei you input 'test' it tries to find a name/var 'test'
#Use raw_input() instead of input()

# Print tasks with number
def view_tasks(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Should receive the users input and add it to the task list (end)
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task added: {task}")

# Remove the task by number provided
def remove_task(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")
    except NameError:
        print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []

    while True:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
               view_tasks(todo_list)
            elif choice == 2:
               add_task(todo_list)
            elif choice == 3:
               remove_task(todo_list)
            elif choice == 4:
               print("Goodbye! Thanks for running this demo")
               break
            else:
              print("Invalid choice. Please enter a number from 1 to 4.")
        except NameError:
            print("Only numbers accepted")
        except ValueError:
            print("Only numbers accepted")

if __name__ == "__main__":
    main()
