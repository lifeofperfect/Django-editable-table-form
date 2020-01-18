from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('testsapi/', views.testsDataAPI, name='list'),
    path('createtest/', views.createTest),
    path('updatetest/', views.updateTest),
    path('deletetest/', views.deleteTest)
]
