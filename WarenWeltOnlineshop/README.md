# WarenWeltOOP – Dokumentation

## Projektübersicht

WarenWeltOOP ist ein objektorientiertes Python-Projekt mit Web-Frontend (Flask), das einen Online-Shop mit Warenkorb, Produktverwaltung und Kundenverwaltung abbildet.

---

## Hauptmodule & Klassen

- **products/**
  - `products.py`: Basisklasse `Product` und ggf. weitere Produktklassen.
  - `books.py`, `electronics.py`, `clothing.py`: Unterklassen für spezifische Produkttypen mit eigenen Attributen (z.B. Gewicht).
- **customer/**
  - `customer.py`: Basisklasse `Customer`.
  - `consumer_customer.py`, `corporate_customer.py`: Unterklassen für Privat- und Firmenkunden.
- **shopping_cart/**
  - `shopping_cart.py`: Verwaltung des Warenkorbs, Methoden zum Hinzufügen/Entfernen von Produkten, Berechnung von Gesamtpreis und Gesamtgewicht.
- **webapp/**
  - `models.py`: SQLAlchemy-Modelle für Datenbank (z.B. `Product`, `User`).
  - `views.py`: Flask-Routen für Shop, Warenkorb, Checkout, Login usw.
  - `templates/`: HTML-Templates für das Web-Frontend (z.B. `cart.html`).

---

## Zentrale Features

- **Produkte:**  
  Verwaltung verschiedener Produkttypen mit Attributen wie Name, Preis, Gewicht, Kategorie.
- **Kunden:**  
  Unterscheidung zwischen Privat- und Firmenkunden, Validierung der Eingaben.
- **Warenkorb:**  
  Produkte können hinzugefügt, entfernt und in der Menge angepasst werden. Gesamtpreis und Gesamtgewicht werden berechnet und angezeigt.
- **Web-Frontend:**  
  Übersichtliche Darstellung aller Funktionen, Interaktion über HTML-Formulare.
- **Datenbank:**  
  Speicherung aller relevanten Daten (Produkte, Kunden, Bestellungen) mit SQLAlchemy.

---

## Sicherheit

- **Passwort-Hashing:**  
  Passwörter werden beim Speichern gehasht (z.B. mit Werkzeug).
- **Login/Logout:**  
  Benutzerverwaltung mit Flask-Login.

---

## Hinweise zur Erweiterung

- Neue Produkttypen können einfach als Unterklassen von `Product` hinzugefügt werden.
- Für neue Felder (z.B. Gewicht) muss die Datenbankstruktur ggf. angepasst werden (Migration).
- Das Web-Frontend kann flexibel erweitert werden, indem neue Templates und Views ergänzt werden.

---

## Start & Nutzung

1. Abhängigkeiten installieren (`pip install -r requirements.txt`)
2. Datenbank initialisieren (ggf. Migration durchführen)
3. Flask-App starten (`flask run`)
4. Web-Frontend im Browser aufrufen

---

## Autoren

- Projektteam WarenWeltOOP
