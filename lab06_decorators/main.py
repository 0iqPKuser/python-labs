from models import RoomStatus
from services import HotelService
from context import operation_logger
import inspect


def inspect_object(obj):
    print("=== ИНФОРМАЦИЯ ОБ ОБЪЕКТЕ ===")
    print(f"Тип: {type(obj).__name__}")
    print(f"Класс: {obj.__class__.__name__}")
    print(f"Атрибуты: {[a for a in dir(obj) if not a.startswith('_')]}")
    if hasattr(obj, 'number'):
        print(f"Номер: {getattr(obj, 'number')}")
    print(f"isinstance Room: {isinstance(obj, type(obj))}")


def main():
    service = HotelService()

    with operation_logger("Добавление номеров"):
        service.add_room("101", "Standard", 2500, 2)
        service.add_room("102", "Luxury", 5000, 2)
        service.add_room("103", "Standard", 2500, 1)

    service.add_guest("Иван Петров", "1234 567890")

    print("\n=== Свободные номера ===")
    for r in service.find_free_rooms():
        print(r.get_report_data())

    service.change_status(1, RoomStatus.OCCUPIED)
    print("\n=== После изменения статуса ===")
    for r in service.rooms:
        print(r.get_report_data())

    print("\n=== Декоратор с параметрами ===")
    service.demonstrate_repeat()

    print()
    inspect_object(service.rooms[0])

    print("\n=== Интроспекция функции ===")
    print(inspect.signature(service.add_room))


if __name__ == "__main__":
    main()