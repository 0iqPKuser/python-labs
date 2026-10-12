from dataclasses import dataclass
from enum import Enum


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
    status: RoomStatus = RoomStatus.FREE


@dataclass
class Booking:
    id: int
    room_id: int
    guest_name: str
    nights: int
    total: float