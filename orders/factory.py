import factory
from .models import PizzaBase, CheeseType, Toppings, Pizza, OrderPizza, Order


class PizzaBaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PizzaBase

    name = factory.Faker("word")


class CheeseTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheeseType

    name = factory.Faker("word")


class ToppingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Toppings

    name = factory.Faker("word")


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    name = factory.Faker("word")
    price = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    status = factory.Faker(
        "random_element",
        elements=["Placed", "Accepted", "Preparing", "Dispatched", "Delivered"],
    )
    total_amount = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )


class OrderPizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderPizza

    pizza_base = factory.SubFactory(PizzaBaseFactory)
    cheese_type = factory.SubFactory(CheeseTypeFactory)
    pizza = factory.SubFactory(PizzaFactory)
    order = factory.SubFactory(OrderFactory)

    @factory.post_generation
    def toppings(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for topping in extracted:
                self.toppings.add(topping)
