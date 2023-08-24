from django.db import models
from utils.models import BaseModel
from django.core.exceptions import ValidationError


class PizzaBase(BaseModel):
    name = models.CharField(max_length=180)

    def __str__(self) -> str:
        return self.name


class CheeseType(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Toppings(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Order(BaseModel):
    STATUS_CHOICES = [
        ("Placed", "Placed"),
        ("Accepted", "Accepted"),
        ("Preparing", "Preparing"),
        ("Dispatched", "Dispatched"),
        ("Delivered", "Delivered"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Placed")
    order_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Order #{self.id} - ({self.status})"

    def save_total_amount(self, amount):
        self.total_amount = amount
        self.save(update_fields=["total_amount", "updated_at"])

    def update_order_status(self, status):
        self.status = status
        self.save(update_fields=["status", "updated_at"])


class Pizza(BaseModel):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"


class OrderPizza(BaseModel):
    pizza_base = models.ForeignKey(
        PizzaBase,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Type of pizza base eg: thin crust, cheese-burst etc",
    )
    cheese_type = models.ForeignKey(
        CheeseType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Type of Cheese eg: mozzarella, cheddar, parmesan",
    )
    toppings = models.ManyToManyField(
        Toppings, related_name="pizzas", blank=True, help_text="Select up to 5 toppings"
    )

    # pizza
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    # order
    order = models.ForeignKey(
        Order, related_name="pizzas", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.pizza.name} with cheese: {self.cheese_type.name} and base: {self.pizza_base.name} and {self.toppings.count()} toppings"

    def assign_order(self, order: Order):
        self.order = order
        self.save(update_fields=["order", "updated_at"])
