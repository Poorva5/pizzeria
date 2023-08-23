from django.contrib import admin
from .models import PizzaBase, CheeseType, Toppings, Order, Pizza, OrderPizza


@admin.register(PizzaBase)
class PizzaBaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(CheeseType)
class CheeseTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "order_time", "total_amount")


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(OrderPizza)
class OrderPizzaAdmin(admin.ModelAdmin):
    list_display = ("pizza_base", "cheese_type", "pizza", "order", "toppings_count")

    def toppings_count(self, obj):
        return obj.toppings.count()

    toppings_count.short_description = "Toppings Count"
