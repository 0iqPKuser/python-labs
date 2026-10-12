from models.entities import RoomStatus
from factories.room_factory import RoomFactory
from exceptions import RoomNotFoundError


class HotelService:
    def __init__(self, repository, pricing_strategy):
        self.repository = repository
        self.pricing = pricing_strategy
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, event):
        for obs in self.observers:
            obs.update(event)

    def add_room(self, room_type, number):
        room = RoomFactory.create(room_type, number)
        self.repository.add(room)
        self.notify(f"Добавлен номер {room.number} ({room.category})")
        return room

    def book_room(self, room_id, nights):
        room = self.repository.get(room_id)
        if room is None:
            raise RoomNotFoundError(f"Номер id={room_id} не найден")
        if room.status != RoomStatus.FREE:
            raise ValueError("Номер занят")
        total = self.pricing.calculate(room.price, nights)
        room.status = RoomStatus.RESERVED
        self.repository.update(room)
        self.notify(f"Номер {room.number} забронирован на {nights} ночей, сумма: {total}")
        return total

    def set_pricing(self, strategy):
        self.pricing = strategy