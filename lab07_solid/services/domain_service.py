from models.entities import Room, RoomStatus, Booking
from interfaces.repository import RoomRepository
from interfaces.services import Notifier, PricingStrategy
from exceptions import RoomNotFoundError


class HotelService:
    def __init__(self, repository: RoomRepository, notifier: Notifier, pricing: PricingStrategy):
        self.repository = repository
        self.notifier = notifier
        self.pricing = pricing

    def add_room(self, number: str, category: str, price: float) -> Room:
        room = Room(id=0, number=number, category=category, price=price)
        self.repository.add(room)
        return room

    def book_room(self, room_id: int, guest_name: str, nights: int) -> Booking:
        room = self.repository.get(room_id)
        if room is None:
            raise RoomNotFoundError(f"Номер id={room_id} не найден")
        if room.status != RoomStatus.FREE:
            raise ValueError("Номер занят")
        total = self.pricing.calculate(room.price, nights)
        room.status = RoomStatus.RESERVED
        self.repository.update(room)
        self.notifier.send(guest_name, f"Номер {room.number} забронирован на {nights} ночей. Сумма: {total}")
        return Booking(id=room_id, room_id=room_id, guest_name=guest_name, nights=nights, total=total)

    def get_free_rooms(self):
        return [r for r in self.repository.get_all() if r.status == RoomStatus.FREE]