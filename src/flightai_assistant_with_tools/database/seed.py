from .db import get_connection, create_tables

SEED_PRICES = [
    ("london", 345),
    ("paris", 573),
    ("tokyo", 1400),
    ("berlin", 342),
    ("kigali", 690),
    ("new york", 899),
    ("dubai", 520),
    ("nairobi", 280),
]

def seed():
	create_tables()
	conn = get_connection()
	try:
		with conn:
			conn.executemany("INSERT OR REPLACE INTO prices (city, price) VALUES (?, ?)",SEED_PRICES,)
			count = conn.execute("SELECT COUNT(*) FROM prices").fetchone()[0]
			print(f"Seeded database with {count} cities.")
	finally:
		conn.close()


if __name__ == "__main__":
	seed()
