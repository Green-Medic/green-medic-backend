from django.urls import path, include

from green_medic.apps.users.views import CustomerView, ShopkeeperView

app_name = "users"

customer_list = CustomerView.as_view({
    'get': 'list',
    'post': 'create'
})
customer_detail = CustomerView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})


shopkeeper_list = ShopkeeperView.as_view({
    'get': 'list',
    'post': 'create'
})
shopkeeper_detail = ShopkeeperView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})


urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),

    path('shopkeepers/', shopkeeper_list, name='shopkeeper_list'),
    path('shopkeepers/<int:pk>/', shopkeeper_detail, name='shopkeeper_detail'),
]
