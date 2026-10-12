import json
import csv
from models import Movie


def save_json(movies, filename="movies.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in movies], f, ensure_ascii=False, indent=4)


def load_json(filename="movies.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Movie.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


def export_csv(movies, filename="movies.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "genre", "year", "rating"])
        for m in movies:
            writer.writerow([m.id, m.title, m.genre, m.year, m.rating])