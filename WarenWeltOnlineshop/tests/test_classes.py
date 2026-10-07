from customer.consumer_customer import Consumer
import random

def generiere_id():
    stellen = random.randint(5, 15)
    untergrenze = 10**(stellen - 1)
    obergrenze = 10**stellen - 1
    return random.randint(untergrenze, obergrenze)

try:
    id = str(generiere_id())
    id_cus = str(generiere_id())
    name = "Leo Löwe"
    address = "Heilbrunn 23 2300 Mödling"
    email = "max.seeberg@gmail.com"
    phone = "+4366423452345"
    password = "sicher123"
    birth = "01.04.1990"

    consumer = Consumer(id, id_cus, name, address, email, phone, password, birth)

    print("ID:", consumer.get_id())
    print("id_cus", consumer.get_id_cus())
    print("Name:", consumer.get_name())
    print("Adresse:", consumer.get_address())
    print("E-Mail:", consumer.get_email())
    print("Telefonnummer:", consumer.get_phone())
    print("Geburtsdatum:", consumer.get_birth())
    print("Alter:", consumer.calc_age())

except ValueError as e:
    print("Fehler:", e)
