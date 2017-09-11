class ToDoList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_file_into_list()

    # 這裡拿一個檔案紀録, 要做的事有那些.
    def load_file_into_list(self):
        tasks = []
        with open(self.file_name, 'r') as file:
            for task in file:
                tasks.append(task.strip())
        return tasks

    def todo_list(self):
        for index, task in enumerate(self.tasks, start=1):
            print('{}) {}'.format(index, task))
            
    # 這裡感覺,  寫的不好, 它參數放 w , 每次寫入會清空, 再重頭寫哎.
    # 案, 它會把檔內的資料, 先全部讀出來, 之後有update的時侯, 
    # 再全部寫回去.
    def write_into_file(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
               file.write('{}\n'.format(task))

    def add_task(self, task):
        self.tasks.append(task)
        self.write_into_file()

    # 還做了一個判庍, 去看 使用者輸入的index,有沒有在裡面.
    # 如果沒有, 就重頭再跑一次.
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
    print('See help:[help]\n') # done 2 # done 5
    print('Get out: [exit]\n') # done 2 # done 5

def run():
    todo_help()
    while True:
        # 這 class , 主要的東西, 就是餵一個檔案進去.
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

"""
第二個參數, 代表只切一個出來.
split(...)
    S.split([sep[, maxsplit]]) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

>>> "aaaa bbb ccc ddd".split(' ')
['aaaa', 'bbb', 'ccc', 'ddd']
>>> "aaaa bbb ccc ddd".split(' ',1)
['aaaa', 'bbb ccc ddd']

"""
