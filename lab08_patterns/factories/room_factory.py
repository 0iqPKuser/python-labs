from models.entities import Room, RoomStatus


class RoomFactory:
    @staticmethod
    def create(room_type: str, number: str) -> Room:
        if room_type == "standard":
            return Room(0, number, "Standard", 2500, 2)
        elif room_type == "luxury":
            return Room(0, number, "Luxury", 5000, 2)
        elif room_type == "family":
            return Room(0, number, "Family", 4000, 4)
        else:
            raise ValueError(f"Неизвестный тип номера: {room_type}")