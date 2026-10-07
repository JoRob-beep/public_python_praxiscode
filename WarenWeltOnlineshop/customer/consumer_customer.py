from customer.customer import Customer
from datetime import datetime, date
from validations.validator import Validator

class Consumer(Customer):
    def __init__(self, id, id_cus, name, address, email, phone, password, birth):
        super().__init__(id, id_cus, name, address, email, phone, password)
        self.birth = birth  # Setter wird verwendet

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if isinstance(value, str):
            if Validator.val_birth(value) is True:
                self._birth = value
            else:
                self._birth = None
        else:
            raise ValueError("Geburtsdatum muss ein String oder datetime.date sein.")

    def get_birth(self):
        return self._birth

    def calc_age(self):
        date_temp = datetime.strptime(self._birth, "%d.%m.%Y").date()

        today = datetime.today().date()
        age = today.year - date_temp.year
        if (today.month, today.day) < (date_temp.month, date_temp.day):
            age -= 1
        return age
