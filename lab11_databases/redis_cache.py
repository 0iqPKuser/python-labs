import redis
import json

class RoomCache:
    def __init__(self, host="localhost", port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def get_room(self, room_id):
        data = self.client.get(f"room:{room_id}")
        return json.loads(data) if data else None

    def set_room(self, room_id, room_data, ttl=60):
        self.client.setex(f"room:{room_id}", ttl, json.dumps(room_data))

    def delete_room(self, room_id):
        self.client.delete(f"room:{room_id}")

    def get_statistics(self):
        data = self.client.get("statistics")
        return json.loads(data) if data else None

    def set_statistics(self, stats, ttl=120):
        self.client.setex("statistics", ttl, json.dumps(stats))