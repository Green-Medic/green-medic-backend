from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from green_medic.apps.users.models import Customer, Shopkeeper


class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        is_authenticated = super().has_permission(request, view)
        is_customer = Customer.objects.filter(user=request.user.id).exists()
        return is_authenticated and is_customer

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'partial_update']:
            return obj == Customer.objects.filter(user=request.user.id).first()
        return False


class IsShopkeeper(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        is_authenticated = super().has_permission(request, view)
        is_shopkeeper = Shopkeeper.objects.filter(user=request.user.id).exists()
        return is_authenticated and is_shopkeeper

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'partial_update']:
            return obj == Shopkeeper.objects.filter(user=request.user.id).first()
        return False


class IsCustomerReadOnly(IsCustomer):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return super(IsCustomer, self).has_permission(request, view)
        return False


class IsShopkeeperReadOnly(IsShopkeeper):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return super(IsShopkeeper, self).has_permission(request, view)
        return False
