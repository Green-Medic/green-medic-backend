from django.urls import path

from green_medic.apps.orders.views import OrderRetrieveUpdateView, OrderListView

app_name = 'order'


urlpatterns = [
    path('', OrderListView.as_view(), name='orders_list'),
    path('<int:pk>/', OrderRetrieveUpdateView.as_view(), name='order_detail'),
]
