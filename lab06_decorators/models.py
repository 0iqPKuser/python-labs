from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class RoomStatus(Enum):
    FREE = "free"
    OCCUPIED = "occupied"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"


@dataclass
class Room:
    id: int
    number: str
    category: str
    price: float
    capacity: int
    status: RoomStatus = RoomStatus.FREE

    def get_report_data(self) -> str:
        return f"Номер {self.number} ({self.category}), {self.price} руб., статус: {self.status.value}"


@dataclass
class Guest:
    id: int
    name: str
    passport: str

    def get_report_data(self) -> str:
        return f"Гость: {self.name}"