from orders.models import Order
from django.utils import timezone
from celery import shared_task
from datetime import timedelta
from celery.utils.log import get_task_logger
from pizzeria.celery_app import app


@app.task(bind=True)
def update_order_status(self):
    orders = Order.objects.all()
    for order in orders:
        time_since_order = (current_time - order.order_time).total_seconds()
        current_time = timezone.now()

        if order.status == "Placed":
            if time_since_order >= 50:
                order.update_order_status("Accepted")

        elif order.status == "Accepted":
            if time_since_order >= 60:
                order.update_order_status("Preparing")

        elif order.status == "Preparing":
            if time_since_order >= 180:
                order.update_order_status("Dispatched")

        elif order.status == "Dispatched":
            if time_since_order >= 300:
                order.update_order_status("Delivered")
