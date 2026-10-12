import sqlite3
from database import Database
from repository import RoomRepository

def main():
    db = Database()
    db.connect()
    repo = RoomRepository(db)

    # Пример: статистика
    print("Статистика:", repo.statistics())

    # Фильтрация
    print("\nНомера от 3000 до 5000:")
    for r in repo.filter_by_price(3000, 5000):
        print(r)

    # Сортировка
    print("\nСортировка по цене (убывание):")
    for r in repo.sort_by_price(desc=True)[:3]:
        print(r)

    # JOIN
    print("\nБронирования:")
    for b in repo.get_rooms_with_bookings():
        print(b)

    # GROUP BY
    print("\nКоличество по типам:")
    for row in repo.count_by_type():
        print(row)

    # Транзакция
    try:
        booking_id = repo.book_room_transaction(1, 1, "2026-03-01", "2026-03-05", 12500)
        print(f"\nТранзакция успешна, booking_id={booking_id}")
    except Exception as e:
        print(f"Ошибка транзакции: {e}")

    db.close()

if __name__ == "__main__":
    main()