import re
from datetime import datetime, date

class Validator:

    @staticmethod
    def val_email(email):
        pattern_email = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.fullmatch(pattern_email, email):
            raise ValueError("Ungültige E-Mail-Adresse.")
        return True

    @staticmethod
    def val_phone(phone):
        pattern_phone = r"^\+?\d{8,19}$"
        if not re.fullmatch(pattern_phone, phone):
            raise ValueError("Ungültige Telefonnummer.")
        return True

    @staticmethod
    def val_name(name):
        pattern_name = r"^[A-Za-zäöüÄÖÜß ]{1,60}$"
        if not re.fullmatch(pattern_name, name):
            raise ValueError("Ungültiger Name.")
        return True

    @staticmethod
    def val_address(address):
        pattern_address = r"^[A-Za-zÄÖÜäöüß0-9\s\-]{5,}$"
        if not re.fullmatch(pattern_address, address):
            raise ValueError("Ungültige Adresse.")
        return True

    @staticmethod
    def val_birth(birth):
        if isinstance(birth, date):
            geburtsdatum = birth
        else:
            try:
                geburtsdatum = datetime.strptime(birth, "%d.%m.%Y").date()
            except ValueError:
                raise ValueError("Ungültiges Datumsformat oder ungültiges Datum.")
        
        heute = date.today()
        if geburtsdatum >= heute:
            raise ValueError("Geburtsdatum liegt in der Zukunft.")
        alter = (heute - geburtsdatum).days // 365
        if alter > 130:
            raise ValueError("Alter ist unrealistisch.")
        return True

    @staticmethod
    def val_id(id):
        pattern_id = r"^[0-9]{5,15}$"
        if not re.fullmatch(pattern_id, id):
            raise ValueError("Ungültige ID.")
        return True

    @staticmethod
    def val_fa_nr(fa_nr):
        pattern_fa_nr = r"^\d{5,15}$"
        if not re.fullmatch(pattern_fa_nr, fa_nr):
            raise ValueError("Ungültige Firmennummer.")
        return True
