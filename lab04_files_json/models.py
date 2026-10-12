from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    title: str
    genre: str
    year: int
    rating: float

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": self.rating
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["genre"],
            data["year"],
            data["rating"]
        )

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.year}) — {self.genre}, рейтинг: {self.rating}"