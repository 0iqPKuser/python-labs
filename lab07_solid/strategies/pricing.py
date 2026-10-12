class StandardPricing:
    def calculate(self, base_price: float, nights: int) -> float:
        return base_price * nights


class SeasonalPricing:
    def calculate(self, base_price: float, nights: int) -> float:
        return base_price * nights * 1.3


class DiscountPricing:
    def calculate(self, base_price: float, nights: int) -> float:
        total = base_price * nights
        if nights >= 7:
            total *= 0.9
        return total