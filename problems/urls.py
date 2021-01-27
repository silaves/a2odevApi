from django.urls import path
from . import views

urlpatterns = [
    path('problem-1/', views.problem_1, name='Problema #1'),
    path('problem-2/', views.problem_2, name='Problema #2'),
    path('problem-3/', views.problem_3, name='Problema #3'),
]