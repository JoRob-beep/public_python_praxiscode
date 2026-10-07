from products.products import Products

class Books(Products):
    def __init__(self, p_id, p_name, p_price, p_weight, p_rating, p_author: str, p_pages: int):
        super().__init__(p_id, p_name, p_price, p_weight, p_rating)
        self.p_author = p_author
        self.p_pages = p_pages

    @property
    def p_author(self):
        return self._p_author

    @p_author.setter
    def p_author(self, value):
        self._p_author = value

    @property
    def p_pages(self):
        return self._p_pages

    @p_pages.setter
    def p_pages(self, value):
        self._p_pages = value


    def get_p_author(self):
        return self._p_author

    def get_p_pages(self):
        return self._p_pages

