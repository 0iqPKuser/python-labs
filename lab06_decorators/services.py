from models import Room, Guest, RoomStatus
from decorators import log_call, measure_time, repeat


class HotelService:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self._next_room_id = 1
        self._next_guest_id = 1

    @log_call
    def add_room(self, number, category, price, capacity):
        room = Room(self._next_room_id, number, category, price, capacity)
        self.rooms.append(room)
        self._next_room_id += 1
        return room

    @log_call
    def add_guest(self, name, passport):
        guest = Guest(self._next_guest_id, name, passport)
        self.guests.append(guest)
        self._next_guest_id += 1
        return guest

    @measure_time
    def find_free_rooms(self):
        return [r for r in self.rooms if r.status == RoomStatus.FREE]

    @repeat(2)
    def demonstrate_repeat(self):
        print("Повторяемое действие")

    def change_status(self, room_id, status):
        for r in self.rooms:
            if r.id == room_id:
                r.status = status
                return r
        raise ValueError(f"Номер id={room_id} не найден")