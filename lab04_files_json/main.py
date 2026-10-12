from services import MovieService
from storage import save_json, load_json, export_csv
from exceptions import MovieNotFoundError, InvalidRatingError


def main():
    service = MovieService()
    service.movies = load_json()
    if service.movies:
        service._next_id = max(m.id for m in service.movies) + 1

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Добавить фильм")
        print("2. Показать все фильмы")
        print("3. Найти фильм по id")
        print("4. Изменить рейтинг")
        print("5. Удалить фильм")
        print("6. Сохранить в JSON")
        print("7. Экспорт в CSV")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                title = input("Название: ")
                genre = input("Жанр: ")
                year = int(input("Год: "))
                rating = float(input("Рейтинг: "))
                m = service.add_movie(title, genre, year, rating)
                print(f"Добавлен: {m}")
            elif choice == "2":
                for m in service.get_all():
                    print(m)
            elif choice == "3":
                mid = int(input("id: "))
                print(service.find_by_id(mid))
            elif choice == "4":
                mid = int(input("id: "))
                new_r = float(input("Новый рейтинг: "))
                service.update_rating(mid, new_r)
                print("Рейтинг обновлён")
            elif choice == "5":
                mid = int(input("id: "))
                service.delete_movie(mid)
                print("Фильм удалён")
            elif choice == "6":
                save_json(service.get_all())
                print("Сохранено в movies.json")
            elif choice == "7":
                export_csv(service.get_all())
                print("Экспортировано в movies.csv")
            elif choice == "0":
                save_json(service.get_all())
                print("Выход. Данные сохранены.")
                break
            else:
                print("Неизвестная команда")
        except ValueError:
            print("Ошибка: некорректный ввод")
        except MovieNotFoundError as e:
            print(f"Ошибка: {e}")
        except InvalidRatingError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()