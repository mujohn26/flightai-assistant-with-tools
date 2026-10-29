import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DB_PATH = BASE_DIR / "data" / "prices.db"

def get_connection():
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)
	return sqlite3.connect(DB_PATH)


def create_tables():
	conn = get_connection()
	try:
		with conn:
			conn.execute("CREATE TABLE IF NOT EXISTS prices(city TEXT PRIMARY KEY, price REAL) ")
	finally:
		conn.close()