class ConsoleNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[NOTIFY -> {recipient}]: {message}")


class EmailNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL -> {recipient}]: {message}")