from validations.validator import Validator
from database_storage import Database_manager

class Customer:
    def __init__(self, id: str, id_cus: str, name: str, address: str, email: str, phone: str, password: str):
        self.id = id
        self.id_cus = id_cus
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return f"Customer({self.id}, {self.id_cus}, {self.name}, {self.address}, {self.email}, {self.phone}, {self.password})"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if Validator.val_id(value) is True:
            self._id = value

    @property
    def id_cus(self):
        return self._id

    @id_cus.setter
    def id_cus(self, value):
        if Validator.val_id(value) is True:
            self._id_cus = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validator.val_name(value) is True:
            self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if Validator.val_address(value) is True:
            self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if Validator.val_email(value) is True:
            self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if Validator.val_phone(value) is True:
            self._phone = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
         self._password = value

    def get_id(self):
        return self._id

    def get_id_cus(self):
        return self._id_cus

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_password(self):
        return self._password


entry = False

if __name__ == "__main__":
    db = Storage(
        host='127.0.0.1',
        user='root',
        password='Swing_and_sing45',
        database='warenwelt'
    )
    db.connect()

    # Letzte Kundenzahl herausfinden
    ## id_counter = 0
    ## = db.load_all_customer()

    # Alle Kunden laden
    alle_k = db.load_all_customer()

    # Letzte ID Nummer:
    last = alle_k[-1]
    id_last = last["id"]
    ##print(id_last)

    # nur nicht das Gleiche speichern:
    # Eingabebereich:
    name = "Robert Maier"
    address = "Mausefalle 1"
    email = "herman.maier@jahoo.com"
    phone = "+43664111111"
    password = "Ich_bin_der_Beste"

    # in Liste suchen:
    for person in alle_k:
        dritter_eintrag = list(person.items())[2][1]  # [1] gibt den Wert zurück
        if dritter_eintrag == name:
            entry = False
            break
        else:
            ##print("❗️Weniger als 3 Einträge:", produkt)
            entry = True

    # Einen Kunden speichern
    if entry is True:
        db.store_customer((id_last+1),(id_last+1),name, address, email, phone, password)
    else:
        print("Name existiert bereits")
    # Den letzten Kunden in der Tabelle laden
    customer = db.load_customer(id_last)
    print(customer)
    '''
    # Kunde laden zum Updaten:
    geladener_kunde = db.load_customer(7)
    print(geladener_kunde)

    if geladener_kunde:
        geladener_kunde.phone = "0987654321"
        db.update_customer(geladener_kunde)
    
    ## Einen Kunden laden
    cus = db.load_customer(7)
    print(cus)
    # Kunden bearbeiten
    ##db.edit_customer(7, {7,7,"Franz Hirsch", "Waldweg 3", "franz.hirsch@gmail.com", "+4366456565656", "Franz_der_Fux"})
    # Produkt bearbeiten
    db.edit_customer(7, {"id": 7, "id_cus":7, "name_cus": "Hans", "address": "Mon Blanc", "email_cus": "hans@glueck.com", "phone_cus": "0664333333", "password_cus": "SchweresPW"})
    # Editiertes Produkt laden
    cus = db.load_customer(7)
    print(cus)
    '''
    db.disconnect()

