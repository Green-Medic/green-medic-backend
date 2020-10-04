from firebase_admin import auth
from firebase_admin.auth import UserNotFoundError


def check_firebase_uid(phone_number, uid):
    try:
        user = auth.get_user_by_phone_number(phone_number)
        return user.uid == uid
    except UserNotFoundError:
        return False


def get_or_create_firebase_test_user(phone_number, display_name=''):
    try:
        user = auth.get_user_by_phone_number(phone_number)
    except UserNotFoundError:
        user = auth.create_user(phone_number=phone_number, display_name=display_name)
    return user
