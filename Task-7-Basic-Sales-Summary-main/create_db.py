import sqlite3
from pathlib import Path

DB_PATH = Path("sales_data.db")

schema = '''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT
);
'''

sample_rows = [
    ("Notebook", 5, 50.0, "2025-08-01"),
    ("Notebook", 3, 50.0, "2025-08-02"),
    ("Pen", 20, 5.0, "2025-08-01"),
    ("Pen", 15, 5.0, "2025-08-03"),
    ("Backpack", 2, 800.0, "2025-08-02"),
    ("Backpack", 1, 800.0, "2025-08-04"),
    ("Marker", 10, 20.0, "2025-08-02"),
    ("Marker", 8, 20.0, "2025-08-03"),
]

if __name__ == "__main__":
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(schema)
        # Keep it reproducible
        cur.execute("DELETE FROM sales")
        cur.executemany(
            "INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)",
            sample_rows
        )
        conn.commit()
    print("Created sales_data.db with sample data.")