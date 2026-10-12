from models import Task


class TaskRepository:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def get_all(self):
        return list(self._tasks.values())

    def get(self, task_id):
        return self._tasks.get(task_id)

    def create(self, title, priority, status, assignee):
        task = Task(self._next_id, title, priority, status, assignee)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def update(self, task_id, data):
        task = self._tasks.get(task_id)
        if task is None:
            return None
        for key, value in data.items():
            if hasattr(task, key):
                setattr(task, key, value)
        return task

    def delete(self, task_id):
        return self._tasks.pop(task_id, None)

    def filter_by_priority(self, priority):
        return [t for t in self._tasks.values() if t.priority == priority]
