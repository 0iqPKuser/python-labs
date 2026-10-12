import socket
from protocol import encode_message, decode_message

HOST = "127.0.0.1"
PORT = 5000


def send_request(sock, command, data=None):
    message = encode_message(command, data or {})
    sock.sendall(message)
    response = b""
    while b"\n" not in response:
        chunk = sock.recv(1024)
        if not chunk:
            break
        response += chunk
    return decode_message(response)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Сервер недоступен")
        return

    while True:
        print("\n=== CLIENT ===")
        print("1. Получить список задач")
        print("2. Получить задачу по id")
        print("3. Создать задачу")
        print("4. Изменить задачу")
        print("5. Удалить задачу")
        print("6. Фильтр по приоритету")
        print("0. Выход")
        choice = input("Выберите: ").strip()

        try:
            if choice == "1":
                resp = send_request(sock, "list")
                print(resp)
            elif choice == "2":
                tid = int(input("ID: "))
                resp = send_request(sock, "get", {"id": tid})
                print(resp)
            elif choice == "3":
                title = input("Название: ")
                priority = input("Приоритет (low/medium/high): ")
                status = input("Статус: ")
                assignee = input("Исполнитель: ")
                resp = send_request(sock, "create", {
                    "title": title, "priority": priority,
                    "status": status, "assignee": assignee
                })
                print(resp)
            elif choice == "4":
                tid = int(input("ID: "))
                field = input("Поле для изменения: ")
                value = input("Новое значение: ")
                resp = send_request(sock, "update", {"id": tid, field: value})
                print(resp)
            elif choice == "5":
                tid = int(input("ID: "))
                resp = send_request(sock, "delete", {"id": tid})
                print(resp)
            elif choice == "6":
                priority = input("Приоритет: ")
                resp = send_request(sock, "filter_by_priority", {"priority": priority})
                print(resp)
            elif choice == "0":
                break
        except socket.timeout:
            print("Тайм-аут ожидания ответа")
        except Exception as e:
            print(f"Ошибка: {e}")

    sock.close()


if __name__ == "__main__":
    main()