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
            return obj == Customer.objects.filter(user=request.user).first()
        return False


class IsShopkeeper(IsAuthenticated):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        is_authenticated = super().has_permission(request, view)
        is_shopkeeper = Shopkeeper.objects.filter(user=request.user).exists()
        return is_authenticated and is_shopkeeper

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'partial_update']:
            return obj == Shopkeeper.objects.filter(user=request.user).first()
        return False
