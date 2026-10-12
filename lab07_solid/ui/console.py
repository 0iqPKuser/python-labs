from services.domain_service import HotelService
from exceptions import RoomNotFoundError


class ConsoleUI:
    def __init__(self, service: HotelService):
        self.service = service

    def run(self):
        while True:
            print("\n=== ГОСТИНИЦА ===")
            print("1. Добавить номер")
            print("2. Показать свободные номера")
            print("3. Забронировать номер")
            print("0. Выход")
            choice = input("Выберите: ").strip()
            try:
                if choice == "1":
                    number = input("Номер: ")
                    category = input("Категория: ")
                    price = float(input("Цена: "))
                    room = self.service.add_room(number, category, price)
                    print(f"Добавлен номер {room.number}")
                elif choice == "2":
                    for r in self.service.get_free_rooms():
                        print(f"  {r.number} ({r.category}) — {r.price} руб.")
                elif choice == "3":
                    rid = int(input("ID номера: "))
                    name = input("Имя гостя: ")
                    nights = int(input("Ночей: "))
                    booking = self.service.book_room(rid, name, nights)
                    print(f"Бронирование оформлено. Сумма: {booking.total}")
                elif choice == "0":
                    break
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
            except RoomNotFoundError as e:
                print(f"Ошибка: {e}")