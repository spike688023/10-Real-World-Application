class ToDoList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_file_into_list()

    def load_file_into_list(self):
        tasks = []
        with open(self.file_name, 'r') as file:
            for task in file:
                tasks.append(task.strip())
        return tasks

    def todo_list(self):
        for index, task in enumerate(self.tasks, start=1):
            print('{}) {}'.format(index, task))
            
    def write_into_file(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
               file.write('{}\n'.format(task))

    def add_task(self, task):
        self.tasks.append(task)
        self.write_into_file()

    def done_task(self, task_index):
        task_exist = False
        for index, task in enumerate(self.tasks, start=1):
            if index == int(task_index):
                self.tasks.remove(task)
                print('{} completed.'.format(task))
                task_exist = True
                self.write_into_file()
        if not task_exist:
            print('There is no open task with index {}'.format(task_index))

def todo_help():
    print('\nWelcome to To Do List APP\n')
    print('* Create new task: [todo TASK]') #todo do homework
    print('* Mark a task as done: [done INDEX]') # ['todo', 'do homework']
    print('See the to-do list: [list]\n') # done 2 # done 5

def run():
    todo_help()
    while True:
        todolist = ToDoList('todolist.txt')
        cmd_detail = input('Enter cmd: ')
        cmd = cmd_detail.split(' ', 1)[0]
        if cmd == 'list':
            todolist.todo_list()
        elif cmd == 'todo':
            task = cmd_detail.split(' ',1)[1]
            todolist.add_task(task)
        elif cmd == 'done':
            task_index = cmd_detail.split(' ',1)[1]
            todolist.done_task(task_index)
        elif cmd == 'help':
            todo_help()
        elif cmd == 'exit':
            break
        
run()
