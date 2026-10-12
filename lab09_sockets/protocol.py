import json


def encode_message(command: str, data: dict) -> bytes:
    message = {"command": command, "data": data}
    return (json.dumps(message, ensure_ascii=False) + "\n").encode("utf-8")


def decode_message(raw: bytes) -> dict:
    return json.loads(raw.decode("utf-8").strip())


def encode_response(status: str, data=None, error=None) -> bytes:
    response = {"status": status}
    if data is not None:
        response["data"] = data
    if error is not None:
        response["error"] = error
    return (json.dumps(response, ensure_ascii=False) + "\n").encode("utf-8")