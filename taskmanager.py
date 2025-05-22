import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Task:
    def __init__(self, task_name, deadline, status='Incomplete'):
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
    def __str__(self):
        return f'{self.task_name} - Deadline: {self.deadline} - Status?: {self.status} '
    
    
task_list = []

def mark_complete():
    if not task_list:
        print('No tasks saved yet.')
    else:
        try:          
            for i, task in enumerate(task_list, start=1):
                print(f'{i}. {task}')  
            mark_selection = int(input('Choose which task you want to mark completed by its number: '))
            current_selection = mark_selection - 1
            if current_selection < 0 or current_selection >= len(task_list):
                print('You entered an invalid number, try again.')
            else:
                sure = input(f'Are you sure to mark this task complete: {task_list[current_selection]}').lower().strip()
                if sure.startswith('y'):
                    task_list[current_selection].status = 'Completed'
                    print('Task successfully completed!')
                elif sure.startswith('n'):
                    print('Operation cancelled.')
        except ValueError:
            print('Please try again and enter a number only.')

def add_task():
    print('Name your task: ')
    task_name = input('> ')
    print('Deadline for the task:')
    task_deadline = input('> ')
    new_task = Task(task_name, task_deadline, status='Incomplete')
    task_list.append(new_task)
    print('Task successfully added!')

def remove_task():
    if not task_list:
        print('No tasks saved yet.')
    else: 
        try:         
            for i, task in enumerate(task_list, start=1):
                print(f'{i}. {task} \n')
            delete_selection = int(input('Choose which task you want to delete by its number: '))
            if delete_selection - 1 < 0 or delete_selection - 1 >= len(task_list):
                print('Please enter a valid number.')
            else:          
                sure = input(f'Are you sure to delete this task (y/n): {task_list[delete_selection - 1].task_name}').lower().strip()
                if sure.startswith('y'):
                    del task_list[delete_selection - 1]
                    print('Task successfully deleted!')
                elif sure.startswith('n') or sure == 'cancel':
                    print('Operation cancelled.')
        except ValueError:
            print('Please enter a valid number.')

def view_task():
    if not task_list:
        print('No tasks saved yet.')
    else:
        for i, task in enumerate(task_list, start=1):
            print(f'{i}. {task}')


print('Welcome to your task manager!')
print('Type "help" for a list of commands.')
while True:
    user_command = input('> ').lower().strip()
    if user_command == 'help':
        print('''help - for help
add - to add a task
del - to delete a task
mark - to mark a task complete
view - to view your current tasks
clear - to clear the terminal
cancel - to cancel any operation you are in
''')
    elif user_command == 'add':
        add_task()
    elif user_command == 'del':
        remove_task()
    elif user_command == 'mark':
        mark_complete()
    elif user_command == 'clear':
        clear()
    elif user_command == 'view':
        view_task()
    else:
        print('I do not understand that, please try something else.')
