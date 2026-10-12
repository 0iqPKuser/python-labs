from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    priority: str
    status: str
    assignee: str

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status,
            "assignee": self.assignee
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["priority"],
            data["status"],
            data["assignee"]
        )