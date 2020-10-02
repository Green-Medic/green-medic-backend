from django.urls import path

from green_medic.apps.medicines.views import MedicineListView, MedicineRetrieveView

app_name = 'medicine'


urlpatterns = [
    path('', MedicineListView.as_view(), name='medicines_list'),
    path('<int:pk>/', MedicineRetrieveView.as_view(), name='medicine_detail'),

]
