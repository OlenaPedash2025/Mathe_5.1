import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_database(self, prepared_data: list):
        if not prepared_data:
            print("No data to insert into the database.")
            return
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DROP TABLE IF EXISTS suppliers")
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS suppliers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price_score REAL NOT NULL,
                        quality_score REAL NOT NULL,
                        eco_score REAL NOT NULL,
                        delivery_score REAL NOT NULL
                    )
                ''')
                cursor.executemany('''
                    INSERT INTO suppliers (name, price_score, quality_score, eco_score, delivery_score)
                    VALUES (?, ?, ?, ?, ?)
                ''', prepared_data)
                conn.commit()
                print("Database 'my_database.db' created and populated successfully!")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    
    def fetch_all_suppliers(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name, price_score, quality_score, eco_score, delivery_score FROM suppliers")
                rows = cursor.fetchall()
                return {row[0]: list(row[1:]) for row in rows}
            # result = {}
            # for row in rows:
            #     name = row[0]
            #     vector = list(row[1:])
            #     result[name] = vector
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return {}
        