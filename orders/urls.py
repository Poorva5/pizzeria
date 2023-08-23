from django.urls import path
from .views import CreateOrderFromPizzasView

urlpatterns = [
    path("create/", CreateOrderFromPizzasView.as_view(), name="create-order"),
]
