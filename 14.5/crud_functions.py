import sqlite3
def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    try:
        cursor.execute('''
           INSERT INTO Users (username, email, age, balance) 
           VALUES (?, ?, ?, 1000)
           ''', (username, email, age))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Пользователь с именем {username} уже существует.")
    finally:
        connection.close()

def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

if __name__ == "__main__":
    initiate_db()