from exceptions import RoomNotFoundError
from strategies.pricing import StandardPricing, SeasonalPricing, WeekendPricing


class ConsoleUI:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            print("\n=== ГОСТИНИЦА ===")
            print("1. Добавить номер (standard/luxury/family)")
            print("2. Показать все номера")
            print("3. Забронировать")
            print("4. Сменить тариф")
            print("0. Выход")
            choice = input("Выберите: ").strip()
            try:
                if choice == "1":
                    room_type = input("Тип (standard/luxury/family): ")
                    number = input("Номер: ")
                    room = self.service.add_room(room_type, number)
                    print(f"Добавлен: {room.number} ({room.category})")
                elif choice == "2":
                    for r in self.service.repository.get_all():
                        print(f"  [{r.id}] {r.number} ({r.category}) — {r.price} руб., статус: {r.status.value}")
                elif choice == "3":
                    rid = int(input("ID: "))
                    nights = int(input("Ночей: "))
                    total = self.service.book_room(rid, nights)
                    print(f"Сумма: {total}")
                elif choice == "4":
                    print("1. Standard  2. Seasonal  3. Weekend")
                    t = input("Выберите тариф: ")
                    if t == "1":
                        self.service.set_pricing(StandardPricing())
                    elif t == "2":
                        self.service.set_pricing(SeasonalPricing())
                    elif t == "3":
                        self.service.set_pricing(WeekendPricing())
                    print("Тариф изменён")
                elif choice == "0":
                    break
            except ValueError as e:
                print(f"Ошибка: {e}")
            except RoomNotFoundError as e:
                print(f"Ошибка: {e}")