from utils.test_utils import APITest
from rest_framework import status
from django import reverse
from orders.factory import PizzaBaseFactory, CheeseTypeFactory, ToppingsFactory


class PizzaBaseListViewTest(APITest):
    def setUp(self):
        self.url = reverse("list-pizza-base")

    def test_list_pizza_base(self):
        PizzaBaseFactory.create_batch(3)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


class CheeseTypeListViewTest(APITest):
    def setUp(self):
        self.url = reverse("list-cheese-type")

    def test_list_cheese_type(self):
        CheeseTypeFactory.create_batch(2)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ToppingsListViewTest(APITest):
    def setUp(self):
        self.url = reverse("list-toppings")

    def test_list_toppings(self):
        ToppingsFactory.create_batch(4)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
