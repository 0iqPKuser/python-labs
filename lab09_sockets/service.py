from repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self):
        return [t.to_dict() for t in self.repository.get_all()]

    def get_task(self, task_id):
        task = self.repository.get(task_id)
        return task.to_dict() if task else None

    def create_task(self, data):
        required = ["title", "priority", "status", "assignee"]
        for field in required:
            if field not in data:
                raise ValueError(f"Отсутствует поле: {field}")
        task = self.repository.create(
            data["title"], data["priority"], data["status"], data["assignee"]
        )
        return task.to_dict()

    def update_task(self, task_id, data):
        task = self.repository.update(task_id, data)
        return task.to_dict() if task else None

    def delete_task(self, task_id):
        return self.repository.delete(task_id)

    def filter_by_priority(self, priority):
        return [t.to_dict() for t in self.repository.filter_by_priority(priority)]