from validations.validator import Validator
from customer.customer import Customer

class Corporate(Customer):
    def __init__(self, id, name, address, email, phone, password, fa_nr):
        super().__init__(id, name, address, email, phone, password)
        self._fa_nr = fa_nr

    @property
    def fa_nr(self):
        return self._fa_nr

    @fa_nr.setter
    def fa_nr(self, value):
        if Validator.val_fa_nr(value) is True:
            self.fa_nr = value

