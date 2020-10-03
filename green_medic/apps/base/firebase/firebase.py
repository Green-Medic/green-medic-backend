# import os
from firebase_admin import auth
from firebase_admin.auth import UserNotFoundError

# from firebase_admin import auth, initialize_app
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keys/green-medicine.json"
# default_app = initialize_app()
#
# # user = auth.get_user_by_phone_number("+8801680177202")
# # auth.get_user_by_email('xxx@xxx.xxx').uid
# # user = auth.get_users()
#
#


def check_firebase_uid(phone_number, uid):
    return True


def get_or_create_firebase_test_user(phone_number, display_name=''):
    try:
        user = auth.get_user_by_phone_number(phone_number)
    except UserNotFoundError:
        user = auth.create_user(phone_number=phone_number, display_name=display_name)
    return user
