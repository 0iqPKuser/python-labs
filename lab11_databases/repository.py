class RoomRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        cursor = self.db.execute("""
            SELECT r.*, rt.name as type_name
            FROM rooms r
            JOIN room_types rt ON r.type_id = rt.id
        """)
        return [dict(row) for row in cursor.fetchall()]

    def get_by_id(self, room_id):
        cursor = self.db.execute("""
            SELECT r.*, rt.name as type_name
            FROM rooms r
            JOIN room_types rt ON r.type_id = rt.id
            WHERE r.id = ?
        """, (room_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def create(self, number, type_id, floor, capacity, price, available=1):
        cursor = self.db.execute(
            "INSERT INTO rooms (number, type_id, floor, capacity, price, available) VALUES (?, ?, ?, ?, ?, ?)",
            (number, type_id, floor, capacity, price, available)
        )
        self.db.commit()
        return cursor.lastrowid

    def update(self, room_id, data):
        fields = []
        values = []
        for key, value in data.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(room_id)
        query = f"UPDATE rooms SET {', '.join(fields)} WHERE id = ?"
        self.db.execute(query, values)
        self.db.commit()

    def delete(self, room_id):
        self.db.execute("DELETE FROM rooms WHERE id = ?", (room_id,))
        self.db.commit()

    def statistics(self):
        cursor = self.db.execute("""
            SELECT COUNT(*) as total, AVG(price) as avg_price,
                   SUM(CASE WHEN available = 1 THEN 1 ELSE 0 END) as available
            FROM rooms
        """)
        return dict(cursor.fetchone())

    def filter_by_price(self, min_price, max_price):
        cursor = self.db.execute(
            "SELECT * FROM rooms WHERE price BETWEEN ? AND ?",
            (min_price, max_price)
        )
        return [dict(row) for row in cursor.fetchall()]

    def sort_by_price(self, desc=False):
        order = "DESC" if desc else "ASC"
        cursor = self.db.execute(f"SELECT * FROM rooms ORDER BY price {order}")
        return [dict(row) for row in cursor.fetchall()]

    def get_rooms_with_bookings(self):
        cursor = self.db.execute("""
            SELECT r.number, g.name as guest_name, b.check_in, b.check_out, b.total
            FROM bookings b
            JOIN rooms r ON b.room_id = r.id
            JOIN guests g ON b.guest_id = g.id
            ORDER BY b.check_in
        """)
        return [dict(row) for row in cursor.fetchall()]

    def count_by_type(self):
        cursor = self.db.execute("""
            SELECT rt.name, COUNT(*) as count
            FROM rooms r
            JOIN room_types rt ON r.type_id = rt.id
            GROUP BY rt.name
            HAVING COUNT(*) > 0
        """)
        return [dict(row) for row in cursor.fetchall()]

    def avg_price_by_type(self):
        cursor = self.db.execute("""
            SELECT rt.name, AVG(r.price) as avg_price
            FROM rooms r
            JOIN room_types rt ON r.type_id = rt.id
            GROUP BY rt.name
        """)
        return [dict(row) for row in cursor.fetchall()]

    def expensive_rooms(self, threshold):
        cursor = self.db.execute(
            "SELECT * FROM rooms WHERE price > ? ORDER BY price DESC",
            (threshold,)
        )
        return [dict(row) for row in cursor.fetchall()]

    def free_rooms(self):
        cursor = self.db.execute("SELECT * FROM rooms WHERE available = 1")
        return [dict(row) for row in cursor.fetchall()]

    def occupied_rooms(self):
        cursor = self.db.execute("SELECT * FROM rooms WHERE available = 0")
        return [dict(row) for row in cursor.fetchall()]

    def guest_bookings(self, guest_id):
        cursor = self.db.execute("""
            SELECT r.number, b.check_in, b.check_out, b.total
            FROM bookings b
            JOIN rooms r ON b.room_id = r.id
            WHERE b.guest_id = ?
        """, (guest_id,))
        return [dict(row) for row in cursor.fetchall()]

    def book_room_transaction(self, room_id, guest_id, check_in, check_out, total):
        try:
            self.db.execute(
                "UPDATE rooms SET available = 0 WHERE id = ? AND available = 1",
                (room_id,)
            )
            cursor = self.db.execute(
                "INSERT INTO bookings (room_id, guest_id, check_in, check_out, total) VALUES (?, ?, ?, ?, ?)",
                (room_id, guest_id, check_in, check_out, total)
            )
            self.db.commit()
            return cursor.lastrowid
        except Exception:
            self.db.rollback()
            raise