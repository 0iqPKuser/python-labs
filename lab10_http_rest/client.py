import requests

BASE_URL = "http://127.0.0.1:5000"


def main():
    while True:
        print("\n=== REST CLIENT ===")
        print("1. Получить список номеров")
        print("2. Получить номер по id")
        print("3. Создать номер")
        print("4. Изменить номер")
        print("5. Удалить номер")
        print("6. Статистика")
        print("0. Выход")
        choice = input("Выберите: ").strip()

        try:
            if choice == "1":
                r = requests.get(f"{BASE_URL}/rooms")
                print(r.status_code, r.json())
            elif choice == "2":
                rid = int(input("ID: "))
                r = requests.get(f"{BASE_URL}/rooms/{rid}")
                print(r.status_code, r.json())
            elif choice == "3":
                data = {
                    "number": input("Номер: "),
                    "type": input("Тип: "),
                    "floor": int(input("Этаж: ")),
                    "capacity": int(input("Вместимость: ")),
                    "price": float(input("Цена: "))
                }
                r = requests.post(f"{BASE_URL}/rooms", json=data)
                print(r.status_code, r.json())
            elif choice == "4":
                rid = int(input("ID: "))
                data = {"price": float(input("Новая цена: "))}
                r = requests.patch(f"{BASE_URL}/rooms/{rid}", json=data)
                print(r.status_code, r.json())
            elif choice == "5":
                rid = int(input("ID: "))
                r = requests.delete(f"{BASE_URL}/rooms/{rid}")
                print(r.status_code)
            elif choice == "6":
                r = requests.get(f"{BASE_URL}/rooms/statistics")
                print(r.status_code, r.json())
            elif choice == "0":
                break
        except requests.ConnectionError:
            print("Сервер недоступен")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()