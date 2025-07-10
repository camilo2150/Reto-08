class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"Bebida: {self.name} ({self.size}) - ${self.price:.2f}"


class Appetizer(MenuItem):
    def __init__(self, name, price, is_vegetarian):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def __str__(self):
        tipo = "Vegetariano" if self.is_vegetarian else "No vegetariano"
        return f"Entrada: {self.name} ({tipo}) - ${self.price:.2f}"


class MainCourse(MenuItem):
    def __init__(self, name, price, spicy_level):
        super().__init__(name, price)
        self.spicy_level = spicy_level

    def __str__(self):
        return f"Plato fuerte: {self.name} (Picante: {self.spicy_level}) - ${self.price:.2f}"


class Dessert(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def __str__(self):
        return f"Postre: {self.name} ({self.calories} cal) - ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    def apply_discount(self):
        total = self.calculate_total()
        if len(self.items) >= 5:
            return total * 0.9  # 10% de descuento
        return total

    def __iter__(self):
        return iter(self.items)


# Crear menú con 10 ítems
menu = [
    Beverage("Coca-Cola", 2.5, "mediana"),
    Beverage("Café", 2.0, "pequeño"),
    Appetizer("Pan de ajo", 3.0, True),
    Appetizer("Alitas", 5.0, False),
    MainCourse("Pizza", 8.5, "medio"),
    MainCourse("Pasta", 9.0, "bajo"),
    MainCourse("Hamburguesa", 7.5, "alto"),
    Dessert("Helado", 3.5, 250),
    Dessert("Tarta", 4.0, 300),
    Dessert("Fruta", 2.0, 100)
]

# Crear pedido
order = Order()
order.add_item(menu[0])  # Coca-Cola
order.add_item(menu[4])  # Pizza
order.add_item(menu[6])  # Hamburguesa
order.add_item(menu[7])  # Helado
order.add_item(menu[2])  # Pan de ajo

# Mostrar totales
print(" Total sin descuento:", order.calculate_total())
print(" Total con descuento:", order.apply_discount())

# Iterar sobre los elementos del pedido
print("\n Elementos del pedido:")
for item in order:
    print("•", item)
