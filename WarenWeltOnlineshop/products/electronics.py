from products.products import Products

class Electronics(Products):
    def __init__(self, p_id, p_name, p_price, p_weight, p_rating, p_lable: str, p_guarantee: int):
        super().__init__(p_id, p_name, p_price, p_weight, p_rating)
        self.p_lable = p_lable
        self.p_guarantee = p_guarantee

    @property
    def p_lable(self):
        return self._p_lable

    @p_lable.setter
    def p_lable(self, value):
        self._p_lable = value

    @property
    def p_guarantee(self):
        return self._p_guarantee

    @p_guarantee.setter
    def p_guarantee(self, value):
        self._p_guarantee = value

    def get_p_lable(self):
        return self._p_lable

    def get_p_guarantee(self):
        return self._p_guarantee


