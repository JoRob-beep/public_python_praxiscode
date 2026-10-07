# Dieses Skript fügt Produkte zur Datenbank hinzu, ohne die Flask-Shell zu benutzen.
# Einfach im Terminal ausführen: python add_products.py

from webapp import create_app, db
from webapp.models import Product

# Flask-App-Kontext erzeugen
app = create_app()
with app.app_context():
    # Beispielprodukte definieren (beliebig anpassen oder erweitern)
    produkte = [
        {
            "name": "T-Shirt",
            "price": 15.99,
            "description": "Shirt mit Superdry darauf.",
            # Hier gibst du die Bild-URL an. Das kann ein Link zu einem Bild im Internet sein,
            # oder ein Pfad zu einem Bild in deinem eigenen static-Ordner, z.B. "/static/images/tshirt.jpg"
            "image_url": "https://image1.superdry.com/static/images/optimised/upload9223368955666318205.jpg",
            "category": "clothing",
            "weight": 0.3  # Gewicht in kg
        },
        {
            "name": "Buch: Steven Hawking",
            "price": 14.49,
            "description": "Eine Kurzgeschichte der Zeit",
            # Auch hier die Bild-URL oder ein relativer Pfad zu deinem static-Ordner
            "image_url": "https://bilder.buecher.de/produkte/67/67620/67620904n.jpg",
            "category": "books",
            "weight": 0.5  # Gewicht in kg
        },
        {
            "name": "Smartwatch",
            "price": 105.99,
            "description": "Extra große Smartwatch",
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/61YksdAioiL._AC_SX569_.jpg",
            "category": "electronics",
            "weight": 2.2  # Gewicht in kg
        }
    ]

    # Produkte zur Datenbank hinzufügen
    for prod in produkte:
        # Prüfen, ob das Produkt schon existiert (nach Name)
        exists = Product.query.filter_by(name=prod["name"]).first()
        if not exists:
            p = Product(**prod)
            db.session.add(p)
            print(f'Produkt hinzugefügt: {prod["name"]}')
        else:
            print(f'Produkt existiert bereits: {prod["name"]}')
    db.session.commit()
    print("Fertig!")