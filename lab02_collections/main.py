def find_by_genre(movies, genre):
    """Поиск фильмов по жанру."""
    return [m for m in movies if m["genre"].lower() == genre.lower()]


def filter_by_rating(movies, min_rating):
    """Фильтрация по рейтингу."""
    return [m for m in movies if m["rating"] >= min_rating]


def average_rating(movies):
    """Средний рейтинг."""
    if not movies:
        return 0
    return sum(m["rating"] for m in movies) / len(movies)


def best_movie(movies):
    """Фильм с максимальным рейтингом."""
    if not movies:
        return None
    return max(movies, key=lambda m: m["rating"])


def unique_genres(movies):
    """Список уникальных жанров."""
    return list({m["genre"] for m in movies})


def sort_by_rating(movies, reverse=True):
    """Сортировка по рейтингу."""
    return sorted(movies, key=lambda m: m["rating"], reverse=reverse)


def main():
    print("=== Каталог фильмов ===")
    try:
        count = int(input("Введите количество фильмов: "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число")
        return

    if count <= 0:
        print("Ошибка: количество должно быть положительным")
        return

    movies = []
    for i in range(count):
        print(f"\nФильм {i + 1}:")
        title = input("Название: ").strip()
        genre = input("Жанр: ").strip()
        try:
            year = int(input("Год выпуска: "))
            rating = float(input("Рейтинг (0-10): "))
        except ValueError:
            print("Ошибка: некорректное числовое значение")
            return
        movies.append({
            "title": title,
            "genre": genre,
            "year": year,
            "rating": rating
        })

    print("\n=== Все фильмы ===")
    for m in movies:
        print(f"{m['title']} ({m['year']}) — {m['genre']}, рейтинг: {m['rating']}")

    genre = input("\nВведите жанр для поиска: ").strip()
    found = find_by_genre(movies, genre)
    print(f"\nНайдено фильмов жанра '{genre}': {len(found)}")
    for m in found:
        print(f"  - {m['title']}")

    try:
        min_rating = float(input("\nВведите минимальный рейтинг для фильтрации: "))
    except ValueError:
        print("Ошибка: некорректное значение")
        return
    filtered = filter_by_rating(movies, min_rating)
    print(f"Фильмов с рейтингом >= {min_rating}: {len(filtered)}")

    print(f"\nСредний рейтинг: {average_rating(movies):.2f}")
    best = best_movie(movies)
    if best:
        print(f"Лучший фильм: {best['title']} ({best['rating']})")
    print(f"Уникальные жанры: {', '.join(unique_genres(movies))}")

    print("\n=== Сортировка по рейтингу (убывание) ===")
    for m in sort_by_rating(movies):
        print(f"{m['title']} — {m['rating']}")


if __name__ == "__main__":
    main()
