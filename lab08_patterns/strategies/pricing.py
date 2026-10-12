class StandardPricing:
    def calculate(self, base_price, nights):
        return base_price * nights


class SeasonalPricing:
    def calculate(self, base_price, nights):
        return base_price * nights * 1.3


class WeekendPricing:
    def calculate(self, base_price, nights):
        return base_price * nights * 1.15