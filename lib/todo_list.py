class TodoList():
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        if task == "":
            raise Exception("Invalid input!")
        
        self._tasks.append(task)

    def complete(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
        else:
            raise KeyError(f"{task} not found")

    def incomplete(self):
        return self._tasks
    