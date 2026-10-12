from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Базовый класс транспортного средства."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self._mileage = value

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_transport_indicator(self):
        pass

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    """Легковой автомобиль."""

    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def get_info(self):
        return f"Автомобиль: {self.brand} {self.model}, пассажиров: {self.passengers}"

    def calculate_transport_indicator(self):
        return self.passengers * 100


class Truck(Vehicle):
    """Грузовик."""

    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def get_info(self):
        return f"Грузовик: {self.brand} {self.model}, грузоподъёмность: {self.capacity} т"

    def calculate_transport_indicator(self):
        return self.capacity * 1000


class Engine:
    """Двигатель (композиция)."""

    def __init__(self, power):
        self.power = power

    def start(self):
        return f"Двигатель мощностью {self.power} л.с. запущен"


class Fleet:
    """Автопарк."""

    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.engine = Engine(150)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_all(self):
        print(f"\n=== Автопарк '{self.name}' ===")
        for v in self.vehicles:
            print(v.get_info())

    def total_indicator(self):
        return sum(v.calculate_transport_indicator() for v in self.vehicles)


def main():
    fleet = Fleet("Городской автопарк")

    car1 = Car("Toyota", "Camry", 2020, 5)
    car2 = Car("Kia", "Rio", 2019, 5)
    truck1 = Truck("Volvo", "FH", 2018, 20)
    truck2 = Truck("MAN", "TGS", 2021, 15)

    for v in [car1, car2, truck1, truck2]:
        fleet.add_vehicle(v)

    # Изменение состояния
    car1.mileage = 15000
    truck1.mileage = 50000

    fleet.show_all()

    print("\n=== Полиморфный вызов ===")
    for v in fleet.vehicles:
        print(f"{v}: показатель = {v.calculate_transport_indicator()}")

    print(f"\nСуммарный показатель автопарка: {fleet.total_indicator()}")
    print(f"Композиция: {fleet.engine.start()}")

    # Проверка инкапсуляции
    try:
        car1.mileage = -100
    except ValueError as e:
        print(f"\nОшибка инкапсуляции: {e}")


if __name__ == "__main__":
    main()