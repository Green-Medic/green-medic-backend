from green_medic.apps.users.tests.factories import CustomerFactory


def test_test():
    customer = CustomerFactory()
    assert customer.user.username
