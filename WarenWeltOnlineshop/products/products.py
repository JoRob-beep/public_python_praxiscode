#from database_storage import Database_manager


class Products():
    def __init__(self, p_id: int, p_name: str, p_price: float, p_weight: float, p_rating: int):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_weight = p_weight
        self.p_ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.p_ratings.append(rating)

    def average_rating(self):
        if not self.p_ratings:
            return 0
        return sum(self.p_ratings) / len(self.p_ratings)

    @property
    def p_id(self):
        return self._p_id

    @p_id.setter
    def p_id(self, value):
        self._p_id = value

    @property
    def p_name(self):
        return self._p_name

    @p_name.setter
    def p_name(self, value):
        self._p_name = value

    @property
    def p_price(self):
        return self._p_price

    @p_price.setter
    def p_price(self, value):
        self._p_price = value

    @property
    def p_weight(self):
        return self._p_weight

    @p_weight.setter
    def p_weight(self, value):
        self._p_weight = value

    @property
    def p_rating(self):
        return self._p_rating

    @p_rating.setter
    def p_rating(self, value):
        self._p_rating = value

    def get_p_id(self):
        return self._p_id

    def get_p_name(self):
        return self._p_name

    def get_p_price(self):
        return self._p_price

    def get_p_weight(self):
        return self._p_weight

    def get_p_rating(self):
        return self._p_rating






