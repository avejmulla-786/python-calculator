class Product:
    count = 0

    def __init__(self, name, price):   
        self.name = name
        self.price = price
        Product.count += 1

    def get_information(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"get count is {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"discount price is = {price - (price * discount/100)}")    


p1 = Product("laptop", 40_000)
p2 = Product("mobile", 25_000)
p3 = Product("headphone", 10_000)

p1.calc_discount(40_000, 10)
p1.get_count()
p1.get_information()