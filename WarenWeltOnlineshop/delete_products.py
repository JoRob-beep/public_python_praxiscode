# Dieses Skript löscht Produkte aus der Datenbank anhand ihres Namens.
# Ausführung im Terminal: python delete_products.py

from webapp import create_app, db
from webapp.models import Product

# Liste der Produktnamen, die gelöscht werden sollen
zu_loeschende_namen = [
    "Bluetooth Kopfhörer"
    # Weitere Produktnamen hier ergänzen
]

app = create_app()
with app.app_context():
    for name in zu_loeschende_namen:
        produkt = Product.query.filter_by(name=name).first()
        if produkt:
            db.session.delete(produkt)
            print(f'Produkt gelöscht: {name}')
        else:
            print(f'Produkt nicht gefunden: {name}')
    db.session.commit()
    print("Löschvorgang abgeschlossen.")