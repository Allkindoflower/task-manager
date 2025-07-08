from database import cursor, conn

print('Task manager')
print('Type add to add a task')

def add_task():
    print('Enter task name:  ')
    new_task = input('> ')
    print('Enter deadline (optional): ')
    new_deadline = input('> ')
    cursor.execute('INSERT INTO tasks (name, deadline) VALUES (?, ?)', (new_task, new_deadline if new_deadline else None))
    conn.commit()
    print('Task successfully added.')
    return new_task

def view_tasks(): 
    cursor.execute('SELECT id, name, deadline, status FROM tasks')
    rows = cursor.fetchall()
    if rows:
        print('Tasks so far: \n')
        for row in rows:         
            status = '✅' if row['status'] else '❌'
            print(f"{row['id']}. {row['name']} | Deadline: {row['deadline']} | Status: {status}")
    else:
        print('No tasks yet')

def delete_task():
    view_tasks()
    print('Which task to delete: ')
    try:
        del_selection = int(input('> '))
    except ValueError:
        print('Please enter a number only.')
        return
    cursor.execute('DELETE FROM tasks WHERE id = ?', (del_selection,))
    conn.commit()
    if cursor.rowcount == 0:
        print('No task by that id.')
    else:
        print('Task deleted.')
   

def logic():
    while True:
        command = input('> ')
        if command == 'add':
            add_task()
        elif command == 'view':
            view_tasks()
        elif command == 'del':
            delete_task()
        else:
            print('...what?')
logic()




