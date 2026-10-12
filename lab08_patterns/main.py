from repositories.memory_repository import InMemoryRoomRepository
from repositories.file_repository import FileRoomRepository
from strategies.pricing import StandardPricing
from services.service import HotelService
from observers.observers import Logger, Notifier, Statistics
from ui.console import ConsoleUI


def main():
    print("Выберите хранилище:")
    print("1. Память")
    print("2. Файл")
    choice = input("Выберите: ").strip()
    if choice == "2":
        repository = FileRoomRepository()
    else:
        repository = InMemoryRoomRepository()

    service = HotelService(repository, StandardPricing())
    service.attach(Logger())
    service.attach(Notifier())
    service.attach(Statistics())

    ui = ConsoleUI(service)
    ui.run()


if __name__ == "__main__":
    main()