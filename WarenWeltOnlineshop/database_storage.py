import pymysql
#from products.electronics import Electronics

class Database_manager:
    def __init__(self, host, user, password, database, port=3306):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._port = port
        self._conn = None

    def connect(self):
        try:
            self._conn = pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                port=self._port,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            print("✅ Verbindung hergestellt.")
        except pymysql.MySQLError as e:
            print(f"❌ Verbindungsfehler: {e}")

    def disconnect(self):
        if self._conn:
            self._conn.close()
            self._conn = None
            print("🔌 Verbindung getrennt.")

### Produkt:

    def store_product(self, id, p_id, p_name, p_price, p_weight, p_ratings):
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO products ( id, p_id, p_name, p_price, p_weight, p_ratings) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (id, p_id, p_name, p_price, p_weight, p_ratings))
            self._conn.commit()
            print("📦 Produkt gespeichert.")

        except pymysql.MySQLError as e:
            print(f"❌ SpeicherFehler: {e}")

    def store_electronics(self, id, p_lable, p_guarantee_years):
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO electronics ( id, p_lable, p_guarantee_years) VALUES (%s, %s, %s)"
                cursor.execute(sql, (id, p_lable, p_guarantee_years))
            self._conn.commit()
            print("📦 Produkt gespeichert.")

        except pymysql.MySQLError as e:
            print(f"❌ SpeicherFehler: {e}")

    def store_clothing(self, id, p_size, p_color, products_id):
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO clothing (id, p_size, p_color, products_id) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id, p_size, p_color, products_id))
            self._conn.commit()
            print("📦 Produkt gespeichert.")

        except pymysql.MySQLError as e:
            print(f"❌ SpeicherFehler: {e}")

    def store_books(self, id, p_author, p_pages, products_id):
        try:
            with self._conn.cursor() as cursor:
                sql = "INSERT INTO books (id, p_author, p_pages, products_id) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id, p_author, p_pages, products_id))
            self._conn.commit()
            print("📦 Produkt gespeichert.")

        except pymysql.MySQLError as e:
            print(f"❌ SpeicherFehler: {e}")

    def load_product(self, p_id):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM products WHERE id = %s"
                cursor.execute(sql, (p_id,))
                result = cursor.fetchone()
            return result
        except pymysql.MySQLError as e:
            print(f"❌ DatenbankFehler: {e}")

    def load_clothing(self, id):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM clothing WHERE id = %s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
            return result
        except pymysql.MySQLError as e:
            print(f"❌ DatenbankFehler: {e}")

    def load_all_products(self):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM products"
                cursor.execute(sql)
                results = cursor.fetchall()
            return results
        except pymysql.MySQLError as e:
            print(f"❌ DatenbankFehler: {e}")

    def edit_product(self, p_id, updated_fields: dict):
        try:
            with self._conn.cursor() as cursor:
                fields = ", ".join([f"{key} = %s" for key in updated_fields])
                values = list(updated_fields.values()) + [p_id]
                sql = f"UPDATE products SET {fields} WHERE id = %s"
                cursor.execute(sql, values)
            self._conn.commit()
            print("✏️ Produkt aktualisiert.")
        except pymysql.MySQLError as e:
            print(f"❌ SpeicherFehler: {e}")

### Kunde:

    def store_customer(self, id: int, id_cus: int, name_cus: str, address_cus:str, email_cus: str, phone_cus: str, password_cus: str):
        with self._conn.cursor() as cursor:
            sql = "INSERT INTO customer ( id, id_cus, name_cus, address_cus, email_cus, phone_cus, password_cus) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (id, id_cus, name_cus, address_cus, email_cus, phone_cus, password_cus))
        self._conn.commit()
        print("📦 Kunde gespeichert.")

    def load_customer(self, id_cus):
        with self._conn.cursor() as cursor:
            sql = "SELECT * FROM customer WHERE id_cus = %s"
            cursor.execute(sql, (id_cus,))
            result = cursor.fetchone()
        return result

    def load_all_customer(self):
        with self._conn.cursor() as cursor:
            sql = "SELECT * FROM customer"
            cursor.execute(sql)
            results = cursor.fetchall()
        return results


    '''
    def edit_customer(self, id_cus, updated_fields: dict):
        with self._conn.cursor() as cursor:
            fields = ", ".join([f"{key} = %s" for key in updated_fields])
            values = list(updated_fields.values()) + [id_cus]
            sql = f"UPDATE customer SET {fields} WHERE id_cus = %s"
            cursor.execute(sql, values)
        self._conn.commit()
        print("✏️ Kunde aktualisiert.")
    

    def update_customer(self, customer):
        with self.conn.cursor() as cursor:
            sql = "UPDATE customers SET id=%s, id_cus=%s, name=%s, address=%s, email=%s, phone=%s, password=%s WHERE id=%s"
            cursor.execute(sql, (customer.id, customer.is_cus, customer.name, customer.address, customer.email, customer.phone, customer.password))
        self.conn.commit()

    def delete_customer(self, customer_id):
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM customers WHERE id=%s"
            cursor.execute(sql, (customer_id,))
        self.conn.commit()
    '''


