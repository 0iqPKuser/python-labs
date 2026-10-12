from exceptions import MovieNotFoundError, InvalidRatingError


class MovieService:
    def __init__(self):
        self.movies = []
        self._next_id = 1

    def add_movie(self, title, genre, year, rating):
        if rating < 0 or rating > 10:
            raise InvalidRatingError("Рейтинг должен быть от 0 до 10")
        movie = Movie(self._next_id, title, genre, year, rating)
        self.movies.append(movie)
        self._next_id += 1
        return movie

    def find_by_id(self, movie_id):
        for m in self.movies:
            if m.id == movie_id:
                return m
        raise MovieNotFoundError(f"Фильм с id={movie_id} не найден")

    def update_rating(self, movie_id, new_rating):
        if new_rating < 0 or new_rating > 10:
            raise InvalidRatingError("Рейтинг должен быть от 0 до 10")
        movie = self.find_by_id(movie_id)
        movie.rating = new_rating

    def delete_movie(self, movie_id):
        movie = self.find_by_id(movie_id)
        self.movies.remove(movie)

    def get_all(self):
        return self.movies