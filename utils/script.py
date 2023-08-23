import random
from django.db import transaction
from orders.models import Pizza, PizzaBase, CheeseType, Toppings, Order, OrderPizza

# List of choices for pizza base, cheese, and toppings
base_choices = ["thin crust", "normal", "cheese burst"]
cheese_choices = ["mozzarella", "cheddar", "parmesan", "blue cheese"]
toppings_choices = [
    "pepperoni",
    "mushrooms",
    "onions",
    "bell-peppers",
    "olives",
    "tomatoes",
    "jalapenos",
]

# Create pizza bases
for base_name in base_choices:
    PizzaBase.objects.create(name=base_name)

# Create cheese types
for cheese_name in cheese_choices:
    CheeseType.objects.create(name=cheese_name)

# Create toppings
for topping_name in toppings_choices:
    Toppings.objects.create(name=topping_name)

# Create a sample order with pizzas
with transaction.atomic():
    order = Order.objects.create(status="Placed", total_amount=0.0)

for _ in range(3):  # Create 3 pizzas in the order
    pizza_base = random.choice(PizzaBase.objects.all())
    cheese_type = random.choice(CheeseType.objects.all())
    toppings = random.sample(list(Toppings.objects.all()), 5)

    pizza_price = 10.0  # Set a default pizza price

    pizza = Pizza.objects.create(
        name=f"{pizza_base.name} with {cheese_type.name} and {len(toppings)} toppings",
        price=pizza_price,
    )

    order_pizza = OrderPizza.objects.create(
        pizza_base=pizza_base, cheese_type=cheese_type, pizza=pizza, order=order
    )
    order_pizza.toppings.set(toppings)

    order.total_amount += pizza_price

order.save()

print("Auto-population completed!")
