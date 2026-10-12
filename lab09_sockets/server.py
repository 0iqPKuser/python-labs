import socket
import logging
from concurrent.futures import ThreadPoolExecutor
from repository import TaskRepository
from service import TaskService
from protocol import decode_message, encode_response

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

HOST = "127.0.0.1"
PORT = 5000

repository = TaskRepository()
service = TaskService(repository)


def handle_client(conn, addr):
    logger.info(f"Client connected: {addr}")
    buffer = b""
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                if not line.strip():
                    continue
                try:
                    message = decode_message(line)
                    command = message.get("command")
                    payload = message.get("data", {})
                    logger.info(f"Command: {command}")

                    if command == "list":
                        response = encode_response("ok", service.list_tasks())
                    elif command == "get":
                        task = service.get_task(payload["id"])
                        if task:
                            response = encode_response("ok", task)
                        else:
                            response = encode_response("error", error="Task not found")
                    elif command == "create":
                        task = service.create_task(payload)
                        response = encode_response("ok", task)
                    elif command == "update":
                        task = service.update_task(payload["id"], payload)
                        if task:
                            response = encode_response("ok", task)
                        else:
                            response = encode_response("error", error="Task not found")
                    elif command == "delete":
                        deleted = service.delete_task(payload["id"])
                        if deleted:
                            response = encode_response("ok", {"deleted": payload["id"]})
                        else:
                            response = encode_response("error", error="Task not found")
                    elif command == "filter_by_priority":
                        tasks = service.filter_by_priority(payload["priority"])
                        response = encode_response("ok", tasks)
                    else:
                        response = encode_response("error", error=f"Unknown command: {command}")

                    conn.sendall(response)
                except Exception as e:
                    logger.error(f"Error processing request: {e}")
                    conn.sendall(encode_response("error", error=str(e)))
    except ConnectionResetError:
        logger.info(f"Client disconnected: {addr}")
    finally:
        conn.close()
        logger.info(f"Connection closed: {addr}")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    logger.info(f"Server started on {HOST}:{PORT}")

    executor = ThreadPoolExecutor(max_workers=10)
    try:
        while True:
            conn, addr = server.accept()
            executor.submit(handle_client, conn, addr)
    except KeyboardInterrupt:
        logger.info("Server stopped")
    finally:
        server.close()


if __name__ == "__main__":
    main()