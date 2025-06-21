import os
import json
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Task:
    def __init__(self, task_name, deadline, status='Incomplete'):
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
    def __str__(self):
        return f'{self.task_name} - Deadline: {self.deadline} - Status?: {self.status} '
    def to_dict(self):
        return {
        'task_name': self.task_name,
        'deadline': self.deadline,
        'status': self.status
        }
    @staticmethod
    def from_dict(data):
        return Task(
        task_name=data['task_name'],
        deadline=data['deadline'],
        status=data.get('status', 'Incomplete')
        )
        
    
class TaskManager:
    def __init__(self):
        self.task_list = []
        self.load_tasks()
    def save_tasks(self, filename='tasks.json'):
        task_dicts = [task.to_dict() for task in self.task_list]
        with open(filename, 'w') as file:
            json.dump(task_dicts, file, indent=4)
    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as file:
                task_dicts = json.load(file)
            self.task_list = [Task.from_dict(d) for d in task_dicts]
        except FileNotFoundError:
            self.task_list = []
    def add_task(self, task_name, task_deadline):
        new_task = Task(task_name, task_deadline, status='Incomplete')
        self.task_list.append(new_task)
        self.save_tasks()
        print('Task successfully added!')
        return new_task
    
    def mark_complete(self):
        if not self.task_list:
            print('No tasks saved yet.')
        else:
            try:          
                for i, task in enumerate(self.task_list, start=1):
                    print(f'{i}. {task}')  
                mark_selection = int(input('Choose which task you want to mark completed by its number: '))
                current_selection = mark_selection - 1
                if current_selection < 0 or current_selection >= len(self.task_list):
                    print('You entered an invalid number, try again.')
                else:
                    sure = input(f'Are you sure to mark this task complete: {self.task_list[current_selection].task_name}').lower().strip()
                    if sure.startswith('y'):
                        self.task_list[current_selection].status = 'Completed'
                        self.save_tasks()
                        print('Task successfully completed!')
                    elif sure.startswith('n'):
                        print('Operation cancelled.')
            except ValueError:
                print('Please try again and enter a number only.')

    def get_task_input(self):
        print('Name your task: ')
        task_name = input('> ')
        print('Deadline for the task:')
        task_deadline = input('> ')
        return task_name, task_deadline
    def remove_task(self):
        if not self.task_list:
            print('No tasks saved yet.')
        else: 
            try:         
                for i, task in enumerate(self.task_list, start=1):
                    print(f'{i}. {task} \n')
                delete_selection = int(input('Choose which task you want to delete by its number: '))
                if delete_selection - 1 < 0 or delete_selection - 1 >= len(self.task_list):
                    print('Please enter a valid number.')
                else:          
                    sure = input(f'Are you sure to delete this task (y/n): {self.task_list[delete_selection - 1].task_name}').lower().strip()
                    if sure.startswith('y'):
                        del self.task_list[delete_selection - 1]
                        self.save_tasks()
                        print('Task successfully deleted!')
                    elif sure.startswith('n') or sure == 'cancel':
                        print('Operation cancelled.')
            except ValueError:
                print('Please enter a valid number.')

    def view_task(self):
        if not self.task_list:
            print('No tasks saved yet.')
        else:
            for task in self.task_list:
                print(task)
                print()
    def main_logic(self):
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
                clear()
                task_name, task_deadline = self.get_task_input()
                self.add_task(task_name, task_deadline)
            elif user_command == 'del':
                clear()
                self.remove_task()
            elif user_command == 'mark':
                clear()
                self.mark_complete()
            elif user_command == 'clear':
                    clear()
            elif user_command == 'view':
                clear()
                self.view_task()
            elif user_command in ('exit', 'quit'):
                self.save_tasks()
                print('Signing off, see you soon!')
                time.sleep(2)
                quit()
            else:
                print('I do not understand that, please try something else.')

print('Welcome to your task manager!')
print('Type "help" for a list of commands.')
print('If you find any bugs, please contact me at bastugugur85@gmail.com')

manager = TaskManager()

manager.main_logic()
