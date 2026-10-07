from customer.corporate_customer import Corporate

class Shopping_cart():
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.sum_total = 0.0

    def add_product(self, product, count=1):
        for _ in range(count):
            self.products.append(product)
        self.calc_sum_total()

    def discard_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.calc_sum_total()

    def clear_cart(self):
        self.products = []
        self.sum_total = 0.0


    def get_count_products(self):    ## um später die Anzahl der Produkte zu haben
        return len(self.products)
    '''
    def calc_sum_total(self):
        ##self.sum_total = sum(product.p_price for product in self.products)
        self.sum_total = sum(product['p_price'] if isinstance(product, dict) else product.p_price for product in self.products)  ## Gesamtsumme
        if isinstance(self.customer, Corporate):  ## 5% Rabatt
            self.sum_total *= 0.95
    '''
    def calc_sum_total(self):
        total = 0.0
        for product in self.products:
            if isinstance(product, dict):
                total += product.get('p_price', 0.0)
            else:
                total += getattr(product, 'p_price', 0.0)
        if isinstance(self.customer, Corporate):
            total *= 0.95  # 5% Rabatt für Firmenkunden
        self.sum_total = total

    def get_count_produkte(self):
        return len(self.products)