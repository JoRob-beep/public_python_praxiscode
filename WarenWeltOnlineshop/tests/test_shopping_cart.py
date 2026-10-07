from customer.consumer_customer import Consumer
from customer.corporate_customer import Corporate
from products.books import Books
from products.electronics import Electronics
from products.clothing import Clothing
from database_storage import Database_manager

from shopping_cart.shopping_cart import Shopping_cart
from shopping_cart.order import Order

def test_shopping():
    print("=== Warenkorb Test ===\n")

    ### --- Produkt aus der Datenbank nehmen --- ###
    if __name__ == "__main__":
        db = Database_manager(
            host='127.0.0.1',
            user='root',
            password='Swing_and_sing45',
            database='warenwelt'
        )
        db.connect()

        # Ein Produkt laden mit
        tshirt = db.load_product(3)
        tshirt2 = db.load_clothing(1)
        laptop = db.load_product(2)
        book = db.load_product(4)

        # Werte extrahieren
        id = tshirt['id']
        name = tshirt['p_name']
        price = str(tshirt['p_price'])
        ratings = tshirt['p_ratings']
        weight = tshirt['p_weight']
        size = tshirt2['p_size']
        color = tshirt2['p_color']

        tshirt3 = [id, name, price, weight, ratings, size, color]
        # Ausgabe
        print(tshirt3)

        db.disconnect()


    # Warenkorb testen (Privatkunde)
    print("\n4. Warenkorb testen - Privatkunde:")
    shopping_cart_consumer = Shopping_cart(Consumer)
    shopping_cart_consumer.add_product(laptop)
    shopping_cart_consumer.add_product(tshirt, 2)
    print(
        f"Warenkorb Privatkunde - Produkte: {shopping_cart_consumer.get_count_products()}, Gesamtsumme: {shopping_cart_consumer.sum_total:.2f}€")

    # Warenkorb testen (Firmenkunde mit Rabatt)
    print("\n5. Warenkorb testen - Firmenkunde (5% Rabatt):")
    shopping_cart_corporate = Shopping_cart(Corporate)
    shopping_cart_corporate.add_product(laptop)
    shopping_cart_corporate.add_product(book, 3)
    print(
        f"Warenkorb Firmenkunde - Produkte: {shopping_cart_corporate.get_count_products()}, Gesamtsumme: {shopping_cart_corporate.sum_total:.2f}€")

    '''
    # Bestellungen erstellen
    print("\n6. Bestellungen erstellen:")
    order_consumer = Order(shopping_cart_consumer)
    bill_consumer = order_consumer.create_bill()
    print(f"Rechnung für Privatkunde erstellt: {bill_consumer}")

    order_corporate = Order(shopping_cart_corporate)
    bill_corporate = order_corporate.create_bill()
    print(f"Rechnung für Firmenkunde erstellt: {bill_corporate}")


    # Produktbewertungen testen
    print("\n7. Produktbewertungen:")
    laptop.add_rating(5)
    laptop.add_rating(4)
    laptop.add_rating(5)
    print(f"Laptop Durchschnittsbewertung: {laptop.durchschnittliche_bewertung():.1f}/5")

    print("\n=== Ende ===")
    '''

if __name__ == "__main__":
    test_shopping()