
def analyze_temperature(temperatures):
    """Вычисляет статистику по температурам."""
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    above_zero = sum(1 for t in temperatures if t > 0)
    hot_days = sum(1 for t in temperatures if t > 25)
    return avg_temp, max_temp, min_temp, above_zero, hot_days


def longest_warm_period(temperatures):
    """Находит наиболее продолжительный период положительной температуры."""
    max_period = 0
    current_period = 0
    for t in temperatures:
        if t > 0:
            current_period += 1
            if current_period > max_period:
                max_period = current_period
        else:
            current_period = 0
    return max_period


def main():
    print("=== Анализ температуры воздуха ===")
    try:
        count = int(input("Введите количество дней наблюдения: "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число")
        return

    if count <= 0:
        print("Ошибка: количество дней должно быть положительным")
        return

    temperatures = []
    for i in range(count):
        try:
            temp = float(input(f"Введите температуру за день {i + 1}: "))
            temperatures.append(temp)
        except ValueError:
            print("Ошибка: необходимо ввести число")
            return

    avg_temp, max_temp, min_temp, above_zero, hot_days = analyze_temperature(temperatures)
    warm_period = longest_warm_period(temperatures)

    print("\n=== Результаты анализа ===")
    print(f"Средняя температура: {avg_temp:.2f}°C")
    print(f"Максимальная температура: {max_temp:.2f}°C")
    print(f"Минимальная температура: {min_temp:.2f}°C")
    print(f"Дней с температурой выше нуля: {above_zero}")
    print(f"Жарких дней (выше 25°C): {hot_days}")
    print(f"Наиболее продолжительный период положительной температуры: {warm_period} дн.")


if __name__ == "__main__":
    main()