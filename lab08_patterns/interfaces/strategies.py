from typing import Protocol


class PricingStrategy(Protocol):
    def calculate(self, base_price: float, nights: int) -> float: ...