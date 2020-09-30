from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from green_medic.apps.orders.models import MedicineQuantity, Order


class MedicineQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineQuantity
        fields = '__all__'


class OrderSerializer(WritableNestedModelSerializer):
    medicines = MedicineQuantitySerializer(many=True)
    conversation = serializers.ListField(child=serializers.JSONField(), required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'lat',
            'long',
            'address',
            'shopkeeper',
            'medicines',
            'conversation',
            'status',
            'system_price',
            'shop_price'
        ]
