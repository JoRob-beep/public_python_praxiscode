from datetime import datetime
from customer.corporate_customer import Corporate
from shopping_cart.shopping_cart import Shopping_cart


class Order:
    def __init__(self, total: float, shopping_cart):
        self.date = datetime.now()
        self.ordered = shopping_cart.products.copy()
        self.total = total
        self.user = shopping_cart.customer

    def create_bill(self):
        bill_file = f"bill_{self.user.id}_{self.date.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(bill_file, 'w', encoding='utf-8') as f:
            f.write("="*50 + "\n")
            f.write("       WARENWELT RECHNUNG\n")
            f.write("=" * 50 + "\n")

            f.write(f"Kunde: {self.user.get_name()}\n")
            f.write(f"E-Mail: {self.user.get_email()}\n")
            f.write(f"Adresse: {self.user.get_address()}\n")
            f.write(f"Bestelldatum: {self.date.strftime('%d.%m.%Y %H:%M')}\n\n")
            f.write(f"Bestellte Produkte: \n")
            f.write("-" *30 + "\n")
            product_counts ={}
            for products in self.ordered:
                if products.name in product_counts:
                    product_counts[products.name]['anzahl']+=1
                else:
                    product_counts[products.name] = {'product': products, 'anzahl': 1}

            for item in product_counts.values():
                product = item['product']
                anzahl = item['anzahl']
                gesamt_preis = product.preis * anzahl
                f.write(f"{product.name} x{anzahl} - {gesamt_preis:.2f}€\n")

            f.write("-" * 30 + "\n")

            if isinstance(self.total, Corporate):
                subtotal = sum(p.preis for p in self.ordered)
                f.write(f"Zwischensummer: {subtotal:.2f}€/n")
                f.write(f"Firmenrabatt (5%): -{subtotal * 0.05:.2f}€/n")

            f.write(f"GESAMTBETRAG: {self.subtotal:.2f}€\n")
            f.write("\nVielen Dank für Ihren Einkauf!\n")


        return bill_file