class Logger:
    def update(self, event):
        print(f"[LOG] {event}")


class Notifier:
    def update(self, event):
        print(f"[NOTIFY] {event}")


class Statistics:
    def __init__(self):
        self.events = []

    def update(self, event):
        self.events.append(event)
        print(f"[STAT] Всего событий: {len(self.events)}")