from database_storage import Storage

if __name__ == "__main__":
    db = Storage(
        host='127.0.0.1',
        user='root',
        password='Swing_and_sing45',
        database='warenwelt'
    )
    db.connect()

    # Produkt 2 speichern (electronics)
    #db.store_product(2, 2, "Laptop (Lenovo)", 800.30, 12.5, 3)
    #db.store_electronics(2, "Lenovo", 1)

    # Produkt 3 speichern (Clothing)
    #db.store_product(3, 3, "Levis-Style", 65, 5, 1)
    #db.store_clothing(1, "45", "Blue", 3)

    # Produkt 4 speichern (Book)
    #db.store_product(4, 4, "Der Dunkle Turm", 26, 2, 1)
    #db.store_books(1, "Steven King", 400, 4)

    db.disconnect()
