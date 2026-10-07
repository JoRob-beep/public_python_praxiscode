import pymysql
from database_storage import *

def connect_to_db():
    try:
        # Verbindung aufbauen
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='Swing_and_sing45',     # Ersetze durch dein Passwort
            database='warenwelt',   # Optional, wenn du direkt eine DB öffnen willst
            port=3306,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        print("✅ Verbindung erfolgreich!")
        return connection

    except pymysql.MySQLError as e:
        print(f"❌ Fehler bei der Verbindung: {e}")
        return None
'''
# Beispielhafte Nutzung:
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        conn.close()


if __name__ == "__main__":
    db = Storage(
        host='127.0.0.1',
        user='root',
        password='Swing_and_sing45',
        database='warenwelt'
    )

    db.connect()

    # Produkt speichern
    ##db.store_product(4,4,"Pullover XL", 25, 3, 8)

    # Ein Produkt laden
    produkt = db.load_product(2)
    print(produkt)

    # Alle Produkte laden
    alle = db.load_all_products()

    print(alle)

    # Produkt bearbeiten
    ##db.edit_product(1, {"p_id": 1, "p_name": "iphone26", "p_price": 1300, "p_weight": 10, "p_ratings": 5})

    db.disconnect()

'''