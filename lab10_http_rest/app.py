from flask import Flask, jsonify, request
from dataclasses import asdict
from repository import RoomRepository
from service import RoomService

app = Flask(__name__)
repository = RoomRepository()
service = RoomService(repository)


def room_to_dict(room):
    return asdict(room)


@app.route("/rooms", methods=["GET"])
def get_rooms():
    available = request.args.get("available")
    if available is not None:
        available = available.lower() == "true"
    rooms = service.get_all(available)
    return jsonify([room_to_dict(r) for r in rooms]), 200


@app.route("/rooms/<int:room_id>", methods=["GET"])
def get_room(room_id):
    room = service.get_by_id(room_id)
    if room is None:
        return jsonify({"error": "Room not found", "code": "ROOM_NOT_FOUND"}), 404
    return jsonify(room_to_dict(room)), 200


@app.route("/rooms", methods=["POST"])
def create_room():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    try:
        room = service.create(data)
        return jsonify(room_to_dict(room)), 201
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


@app.route("/rooms/<int:room_id>", methods=["PUT"])
def update_room(room_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    room = service.update(room_id, data)
    if room is None:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room_to_dict(room)), 200


@app.route("/rooms/<int:room_id>", methods=["PATCH"])
def patch_room(room_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    room = service.update(room_id, data)
    if room is None:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room_to_dict(room)), 200


@app.route("/rooms/<int:room_id>", methods=["DELETE"])
def delete_room(room_id):
    deleted = service.delete(room_id)
    if deleted is None:
        return jsonify({"error": "Room not found"}), 404
    return "", 204


@app.route("/rooms/statistics", methods=["GET"])
def statistics():
    return jsonify(service.statistics()), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)