class InternetShop:
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name):
        self.shop_name = shop_name
        self.product_name = product_name
        self.country_of_origin = country_of_origin
        self.payment_method = payment_method
        self.purchase_amount = purchase_amount
        self.sale_date = sale_date
        self.buyer_name = buyer_name

    def __str__(self):
        return f"Название магазина: {self.shop_name} Название товара: {self.product_name} Страна производитель: {self.country_of_origin} Вид оплаты: {self.payment_method}\nСумма покупки: {self.purchase_amount}\nДата продажи: {self.sale_date}\nФИО покупателя: {self.buyer_name}"

class LivingRoomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name,
                 furniture_type, manufacturer, price):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.furniture_type = furniture_type
        self.manufacturer = manufacturer
        self.price = price
    def __str__(self):
        return super().__str__() + f"Тип мебели для гостиных: {self.furniture_type} Производитель: {self.manufacturer} Цена: {self.price}"

class KitchenFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name,
                 length, height, width, material, price):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.length = length
        self.height = height
        self.width = width
        self.material = material
        self.price = price
    def __str__(self):
        return super().__str__() + f"Длина: {self.length} Высота: {self.height} Ширина: {self.width} Материал: {self.material} Цена: {self.price}"
class BathroomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name, price):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price
    def __str__(self):
        return super().__str__() + f"Цена: {self.price}"
