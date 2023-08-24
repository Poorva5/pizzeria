from django.urls import path
from .views import (
    CreateOrderFromPizzasView,
    PizzaBaseListView,
    CheeseTypeListView,
    ToppingsListView,
    TrackOrderView,
)

urlpatterns = [
    path("create/", CreateOrderFromPizzasView.as_view(), name="create-order"),
    path("track-order/<int:order_id>/", TrackOrderView.as_view(), name="track-order"),
    path("list-pizza-base/", PizzaBaseListView.as_view(), name="list-pizza-base"),
    path("list-cheese-type/", CheeseTypeListView.as_view(), name="list-cheese-type"),
    path("list-toppings/", ToppingsListView.as_view(), name="list-toppings"),
]
