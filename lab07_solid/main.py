from repositories.memory_repository import InMemoryRoomRepository
from infrastructure.notifier import ConsoleNotifier
from strategies.pricing import StandardPricing
from services.domain_service import HotelService
from ui.console import ConsoleUI


def main():
    repository = InMemoryRoomRepository()
    notifier = ConsoleNotifier()
    pricing = StandardPricing()
    service = HotelService(repository, notifier, pricing)
    ui = ConsoleUI(service)
    ui.run()


if __name__ == "__main__":
    main()