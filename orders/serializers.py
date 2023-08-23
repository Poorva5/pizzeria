from rest_framework import serializers
from .models import PizzaBase, CheeseType, Toppings, Order, Pizza, OrderPizza


class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = ["id", "name"]


class CheeseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheeseType
        fields = ["id", "name"]


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = ["id", "name"]


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ["id", "name", "price"]


class OrderPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPizza
        fields = ["id", "pizza_base", "cheese_type", "toppings", "pizza", "order"]

    def validate_toppings(self, value):
        if len(value) > 5:
            raise serializers.ValidationError(
                "A maximum of 5 toppings are allowed per pizza."
            )
        return value


class OrderPizzaDetailSerializer(serializers.ModelSerializer):
    pizza_base = PizzaBaseSerializer()
    cheese_type = CheeseTypeSerializer()
    toppings = ToppingsSerializer(many=True)

    class Meta:
        model = OrderPizza
        fields = ["id", "pizza_base", "cheese_type", "toppings", "pizza"]


class OrderSerializer(serializers.ModelSerializer):
    pizza = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "status", "order_time", "total_amount", "pizza"]

    @staticmethod
    def get_pizza(obj):
        return OrderPizzaDetailSerializer(
            OrderPizza.objects.filter(order=obj), many=True
        ).data
