class InMemoryRoomRepository:
    def __init__(self):
        self._rooms = {}
        self._next_id = 1

    def add(self, room):
        if room.id == 0:
            room.id = self._next_id
            self._next_id += 1
        self._rooms[room.id] = room

    def get(self, room_id):
        return self._rooms.get(room_id)

    def get_all(self):
        return list(self._rooms.values())

    def update(self, room):
        self._rooms[room.id] = room

    def delete(self, room_id):
        self._rooms.pop(room_id, None)