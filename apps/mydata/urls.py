from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.MyDataAPIView.as_view(), name='myData_list'),
]