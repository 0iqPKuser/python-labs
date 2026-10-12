import json
from models.entities import Room, RoomStatus


class FileRoomRepository:
    def __init__(self, filename="rooms.json"):
        self.filename = filename
        self._rooms = {}
        self._load()

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    room = Room(
                        id=item["id"],
                        number=item["number"],
                        category=item["category"],
                        price=item["price"],
                        capacity=item["capacity"],
                        status=RoomStatus(item["status"])
                    )
                    self._rooms[room.id] = room
        except FileNotFoundError:
            pass

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([
                {
                    "id": r.id, "number": r.number, "category": r.category,
                    "price": r.price, "capacity": r.capacity, "status": r.status.value
                } for r in self._rooms.values()
            ], f, ensure_ascii=False, indent=4)

    def add(self, room):
        if room.id == 0:
            room.id = max(self._rooms.keys(), default=0) + 1
        self._rooms[room.id] = room
        self._save()

    def get(self, room_id):
        return self._rooms.get(room_id)

    def get_all(self):
        return list(self._rooms.values())

    def update(self, room):
        self._rooms[room.id] = room
        self._save()

    def delete(self, room_id):
        self._rooms.pop(room_id, None)
        self._save()