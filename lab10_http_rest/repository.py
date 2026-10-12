from models import Room


class RoomRepository:
    def __init__(self):
        self._rooms = {}
        self._next_id = 1

    def get_all(self):
        return list(self._rooms.values())

    def get_by_id(self, room_id):
        return self._rooms.get(room_id)

    def create(self, number, type_, floor, capacity, price, available=True):
        room = Room(self._next_id, number, type_, floor, capacity, price, available)
        self._rooms[room.id] = room
        self._next_id += 1
        return room

    def update(self, room_id, data):
        room = self._rooms.get(room_id)
        if room is None:
            return None
        for key, value in data.items():
            if hasattr(room, key):
                setattr(room, key, value)
        return room

    def delete(self, room_id):
        return self._rooms.pop(room_id, None)