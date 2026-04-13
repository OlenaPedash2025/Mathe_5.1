import sqlite3
from data_provider import JSONDataProvider



def create_database():
    raw_data = JSONDataProvider.load_from_file("data/data.json")
    if not raw_data:
        print("No data to populate the database.")
        return
    
    prepared_data = []
    for item in raw_data:
        name = item.get("name")
        vector = item.get("vector", [])
        if len(vector) != 4:
            print(f"Skipping {name}: Expected 4 dimensions, got {len(vector)}")
            continue
        prepared_data.append((name, *vector))
        
            
    conn = sqlite3.connect('my_database.db')
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
    conn.close()
    print("Database 'my_database.db' created and populated successfully!")

def fetch_data(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, price_score, quality_score, eco_score, delivery_score FROM suppliers")
        rows = cursor.fetchall()
        conn.close()
        return {row[0]: list(row[1:]) for row in rows}
    # result = {}
    # for row in rows:
    #     name = row[0]
    #     vector = list(row[1:])
    #     result[name] = vector
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
        return {}   