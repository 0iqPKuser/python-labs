from dataclasses import dataclass, field
from enum import Enum
from typing import List


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