

from functools import reduce
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    genre: str
    year: int
    rating: float
    duration: int  # минуты


# ---------- Функции высшего порядка ----------

def filter_objects(objects, predicate):
    """Функция высшего порядка: фильтрация по предикату."""
    return list(filter(predicate, objects))


def transform_objects(objects, operation):
    """Функция высшего порядка: преобразование."""
    return list(map(operation, objects))


def sort_objects(objects, key_function, reverse=False):
    """Функция высшего порядка: сортировка по ключу."""
    return sorted(objects, key=key_function, reverse=reverse)


# ---------- Генераторы ----------

def movies_by_genre(movies, genre):
    """Генератор фильмов заданного жанра."""
    for m in movies:
        if m.genre.lower() == genre.lower():
            yield m


def long_movies(movies, min_duration):
    """Генератор длинных фильмов."""
    for m in movies:
        if m.duration >= min_duration:
            yield m


# ---------- Собственный итератор ----------

class MovieIterator:
    def __init__(self, movies):
        self.movies = movies
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.movies):
            raise StopIteration
        result = self.movies[self.index]
        self.index += 1
        return result


def main():
    movies = [
        Movie("Inception", "Sci-Fi", 2010, 8.8, 148),
        Movie("Titanic", "Drama", 1997, 7.8, 195),
        Movie("Interstellar", "Sci-Fi", 2014, 8.6, 169),
        Movie("Joker", "Drama", 2019, 8.4, 122),
        Movie("Dune", "Sci-Fi", 2021, 8.0, 155),
    ]

    print("=== Все фильмы ===")
    for m in movies:
        print(m)

    # map()
    titles = transform_objects(movies, lambda m: m.title)
    print(f"\nНазвания через map(): {titles}")

    # filter()
    high_rated = filter_objects(movies, lambda m: m.rating >= 8.5)
    print(f"\nФильмы с рейтингом >= 8.5:")
    for m in high_rated:
        print(f"  {m.title} — {m.rating}")

    # sorted с key
    by_duration = sort_objects(movies, key_function=lambda m: m.duration)
    print(f"\nСортировка по длительности:")
    for m in by_duration:
        print(f"  {m.title} — {m.duration} мин")

    # reduce
    total_duration = reduce(lambda acc, m: acc + m.duration, movies, 0)
    print(f"\nСуммарная длительность (reduce): {total_duration} мин")

    # comprehension
    sci_fi_titles = [m.title for m in movies if m.genre == "Sci-Fi"]
    print(f"\nSci-Fi фильмы (comprehension): {sci_fi_titles}")

    # any / all
    has_long = any(m.duration > 180 for m in movies)
    all_rated = all(m.rating > 7 for m in movies)
    print(f"\nЕсть фильм длиннее 180 мин: {has_long}")
    print(f"Все фильмы с рейтингом > 7: {all_rated}")

    # Генератор
    print("\n=== Sci-Fi фильмы (генератор) ===")
    for m in movies_by_genre(movies, "Sci-Fi"):
        print(f"  {m.title}")

    # Собственный итератор
    print("\n=== Собственный итератор ===")
    it = MovieIterator(movies[:3])
    for m in it:
        print(f"  {m.title}")

    # Демонстрация ленивости
    import sys
    list_comp = [x * x for x in range(10000)]
    gen_expr = (x * x for x in range(10000))
    print(f"\nРазмер списка: {sys.getsizeof(list_comp)} байт")
    print(f"Размер генератора: {sys.getsizeof(gen_expr)} байт")


if __name__ == "__main__":
    main()