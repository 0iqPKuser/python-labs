from repository import RoomRepository


class RoomService:
    def __init__(self, repository: RoomRepository):
        self.repository = repository

    def get_all(self, available=None):
        rooms = self.repository.get_all()
        if available is not None:
            rooms = [r for r in rooms if r.available == available]
        return rooms

    def get_by_id(self, room_id):
        return self.repository.get_by_id(room_id)

    def create(self, data):
        if data["price"] <= 0:
            raise ValueError("Цена должна быть положительной")
        if data["capacity"] <= 0:
            raise ValueError("Вместимость должна быть положительной")
        return self.repository.create(
            data["number"], data["type"], data["floor"],
            data["capacity"], data["price"], data.get("available", True)
        )

    def update(self, room_id, data):
        return self.repository.update(room_id, data)

    def delete(self, room_id):
        return self.repository.delete(room_id)

    def statistics(self):
        rooms = self.repository.get_all()
        if not rooms:
            return {"total": 0, "average_price": 0, "available": 0}
        return {
            "total": len(rooms),
            "average_price": sum(r.price for r in rooms) / len(rooms),
            "available": sum(1 for r in rooms if r.available)
        }