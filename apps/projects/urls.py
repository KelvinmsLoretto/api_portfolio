from django.urls import path
from .views import TecnologyListAPIView, ProjectListAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project_list'),
    path('tecnologies/', TecnologyListAPIView.as_view(), name='tecnologies_list'),
]