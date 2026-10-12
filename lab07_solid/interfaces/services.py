from typing import Protocol


class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> None: ...


class PricingStrategy(Protocol):
    def calculate(self, base_price: float, nights: int) -> float: ...