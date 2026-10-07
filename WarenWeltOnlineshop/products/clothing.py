from products.products import Products

class Clothing(Products):
    def __init__(self, p_id, p_name, p_price, p_weight, p_rating, p_size: str, p_color: str):
        super().__init__(p_id, p_name, p_price, p_weight, p_rating)
        self.p_size = p_size
        self.p_color = p_color

    @property
    def p_size(self):
        return self._p_size

    @p_size.setter
    def p_size(self, value):
        self._p_size = value

    @property
    def p_color(self):
        return self._p_color

    @p_color.setter
    def p_color(self, value):
        self._p_color = value


    def get_p_size(self):
        return self._p_size

    def get_p_color(self):
        return self._p_color

