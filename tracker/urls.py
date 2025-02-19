from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-topic/', views.add_topic, name='add_topic'),
    path('todays-revision/', views.todays_revision, name='todays_revision'),
]
