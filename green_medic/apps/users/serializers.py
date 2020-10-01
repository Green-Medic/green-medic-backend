from django.contrib.auth.models import User
from django.db import transaction
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, status
from django.contrib.auth.hashers import make_password

from green_medic.apps.base.firebase.firebase import check_firebase_uid
from green_medic.apps.users.models import Customer, Shopkeeper


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CustomerSerializer(WritableNestedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = [
            'id',
            'user',
            'fcm_token',
            'name',
            'age',
            'gender',
            'lat',
            'long',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        if not check_firebase_uid(uid=user_data.get('password'), phone_number=user_data.get('username')):
            raise serializers.ValidationError({'message': 'Invalid  uid or phone number'},
                                              code=status.HTTP_401_UNAUTHORIZED)
        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            customer = Customer.objects.create(**validated_data, user=user)
        return customer


class ShopkeeperSerializer(WritableNestedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Shopkeeper
        fields = [
            'id',
            'user',
            'fcm_token',
            'name',
            'shop_name',
            'address',
            'lat',
            'long',
            'registration_number',
            'nid',
            'status',
        ]
        read_only_fields = ['status', ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        if not check_firebase_uid(uid=user_data.get('password'), phone_number=user_data.get('username')):
            raise serializers.ValidationError({'message': 'Invalid  uid or phone number'},
                                              code=status.HTTP_401_UNAUTHORIZED)
        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            shopkeeper = Shopkeeper.objects.create(**validated_data, user=user)
        return shopkeeper
