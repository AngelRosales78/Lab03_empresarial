from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:pk>/', views.exam_detail, name='exam_detail'),
    path('exam/<int:pk>/add-question/', views.add_question, name='add_question'),
]
