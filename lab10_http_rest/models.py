from dataclasses import dataclass


@dataclass
class Room:
    id: int
    number: str
    type: str
    floor: int
    capacity: int
    price: float
    available: bool