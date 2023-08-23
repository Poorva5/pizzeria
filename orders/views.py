from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import (
    PizzaBaseSerializer,
    CheeseTypeSerializer,
    ToppingsSerializer,
    OrderSerializer,
    OrderPizzaSerializer,
)
from .models import PizzaBase, CheeseType, Toppings, Order


class CreateOrderFromPizzasView(APIView):
    def post(self, request):
        data = request.data
        orderpizza_serializer = OrderPizzaSerializer(data=data, many=True)

        if orderpizza_serializer.is_valid():
            # get all pizza order instances
            orderpizza_instances = orderpizza_serializer.save()

            # create new order instance
            order = Order.objects.create(total_amount=0)

            for orderpizza in orderpizza_instances:
                # assign order to pizza instance
                orderpizza.assign_order(order)

            # update total amount on order
            total_amount = sum(
                orderpizza.pizza.price for orderpizza in orderpizza_instances
            )
            order.save_total_amount(total_amount)

            order_serializer = OrderSerializer(order).data
            return Response(order_serializer, status=status.HTTP_201_CREATED)

        return Response(
            orderpizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PizzaBaseListView(generics.ListAPIView):
    queryset = PizzaBase.objects.all()
    serializer_class = PizzaBaseSerializer


class CheeseTypeListView(generics.ListAPIView):
    queryset = CheeseType.objects.all()
    serializer_class = CheeseTypeSerializer


class ToppingsListView(generics.ListAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
