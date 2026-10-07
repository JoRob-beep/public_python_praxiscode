from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file
from flask_login import login_required, current_user
from .models import Product
from . import db
import io
import tempfile
import os
from flask import send_file, send_from_directory

# OOP-Klassen einbinden
from products.books import Books
from products.electronics import Electronics
from products.clothing import Clothing

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('views.shop'))


@views.route('/shop')
def shop():
    # Kategorie aus Query-Parameter lesen
    category = request.args.get('category')
    if category in ['books', 'electronics', 'clothing']:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    return render_template("shop.html", products=products, user=current_user, selected_category=category)

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product, user=current_user)

@views.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    flash('Produkt zum Warenkorb hinzugefügt!', category='success')
    return redirect(url_for('views.shop'))

def get_cart_items():
    cart = session.get('cart', {})
    items = []
    for product_id, qty in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            items.append({'product': product, 'qty': qty})
    return items

def get_shipping_cost(shipping_method):
    if shipping_method == 'standard':
        return 6.0
    elif shipping_method == 'express':
        return 11.0
    return 0.0

@views.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    items = get_cart_items()
    total = sum(item['product'].price * item['qty'] for item in items)
    discount = 0
    if current_user.company_number:
        discount = total * 0.05
    total_after_discount = total - discount

    # Gesamtgewicht berechnen
    total_weight = sum(getattr(item['product'], 'weight', 0) * item['qty'] for item in items)

    # Liefermethode aus Session oder Standard
    shipping_method = session.get('shipping_method')
    if shipping_method not in ['pickup', 'standard', 'express']:
        shipping_method = 'pickup'  # Standard auf 'pickup' setzen
    shipping_cost = get_shipping_cost(shipping_method)
    total_with_shipping = total_after_discount + shipping_cost

    return render_template(
        "cart.html",
        products=items,
        total=total,
        discount=discount,
        total_after_discount=total_after_discount,
        shipping_method=shipping_method,
        shipping_cost=shipping_cost,
        total_with_shipping=total_with_shipping,
        total_weight=total_weight,  # <-- hinzugefügt
        user=current_user
    )

@views.route('/update-cart', methods=['POST'])
@login_required
def update_cart():
    cart = session.get('cart', {})
    # Mengen aktualisieren
    for key, value in request.form.items():
        if key.startswith('qty_'):
            product_id = key[4:]
            try:
                qty = int(value)
                if qty > 0:
                    cart[product_id] = qty
                else:
                    cart.pop(product_id, None)
            except ValueError:
                continue
    # Liefermethode speichern
    shipping_method = request.form.get('shipping_method', 'pickup')
    session['shipping_method'] = shipping_method
    session['cart'] = cart
    return redirect(url_for('views.cart'))

@views.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    return redirect(url_for('views.cart'))

@views.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    items = get_cart_items()
    total = sum(item['product'].price * item['qty'] for item in items)
    discount = 0
    if current_user.company_number:
        discount = total * 0.05
    total_after_discount = total - discount

    shipping_method = session.get('shipping_method')
    if shipping_method not in ['pickup', 'standard', 'express']:
        shipping_method = 'pickup'
    shipping_cost = get_shipping_cost(shipping_method)
    total_with_shipping = total_after_discount + shipping_cost

    if request.method == 'POST':
        invoice_lines = []
        invoice_lines.append("Rechnung\n")
        invoice_lines.append(f"Kunde: {current_user.first_name} ({current_user.email})\n")
        invoice_lines.append("--------------------------------------------------\n")
        for item in items:
            name = item['product'].name
            qty = item['qty']
            price = item['product'].price
            weight = getattr(item['product'], 'weight', 0)
            invoice_lines.append(f"{name} | Menge: {qty} | Einzelpreis: {price:.2f} € | Gewicht: {weight} kg | Gesamt: {price*qty:.2f} €\n")
        invoice_lines.append("--------------------------------------------------\n")
        invoice_lines.append(f"Zwischensumme: {total:.2f} €\n")
        if discount > 0:
            invoice_lines.append(f"Firmenkundenrabatt: -{discount:.2f} €\n")
        invoice_lines.append(f"Lieferkosten: {shipping_cost:.2f} €\n")
        invoice_lines.append(f"Gesamtbetrag: {total_with_shipping:.2f} €\n")
        invoice_lines.append("--------------------------------------------------\n")
        invoice_lines.append("Vielen Dank für Ihren Einkauf!\n")

        invoice_text = ''.join(invoice_lines)

        temp_dir = tempfile.gettempdir()
        temp_dir = tempfile.gettempdir()
        invoice_path = os.path.join(temp_dir, f"rechnung_{current_user.id}.txt")
        with open(invoice_path, "w", encoding="utf-8") as f:
            f.write(invoice_text)

        session.pop('cart', None)
        session.pop('shipping_method', None)
        # Nur hier flash
        flash('Vielen Dank für Ihre Bestellung! Ihre Rechnung steht zum Download bereit.', 'success')
        return redirect(url_for('views.invoice_ready'))

    return render_template(
        "checkout.html",
        products=items,
        total=total,
        discount=discount,
        total_after_discount=total_after_discount,
        shipping_method=shipping_method,
        shipping_cost=shipping_cost,
        total_with_shipping=total_with_shipping,
        user=current_user
    )

@views.route('/invoice-ready')
@login_required
def invoice_ready():
    return render_template("invoice_ready.html", user=current_user)

@views.route('/download-invoice')
@login_required
def download_invoice():
    import tempfile, os
    temp_dir = tempfile.gettempdir()
    invoice_path = os.path.join(temp_dir, f"rechnung_{current_user.id}.txt")
    rechnung_name = f"rechnung_{current_user.first_name}.txt"
    if os.path.exists(invoice_path):
        return send_file(invoice_path, mimetype='text/plain', as_attachment=True, download_name=rechnung_name)
    flash("Rechnung nicht gefunden.", "error")
    return redirect(url_for('views.shop'))