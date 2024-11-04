import sqlite3

def add_products():
    connection = sqlite3.connect(r"C:\Users\nix95\Desktop\Обучение программированию\модули\5 классы и объекты\products.db")
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    if count == 0:
        products = [
            ("Product1", "Описание продукта 1", 100),
            ("Product2", "Описание продукта 2", 200),
            ("Product3", "Описание продукта 3", 300),
            ("Product4", "Описание продукта 4", 400)
        ]

        cursor.executemany('''
        INSERT INTO Products (title, description, price) 
        VALUES (?, ?, ?)
        ''', products)

        connection.commit()
    else:
        print("Продукты уже добавлены в базу данных.")

    connection.close()

add_products()
