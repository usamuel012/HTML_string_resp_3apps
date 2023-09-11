from django.urls import path
from app2.views import *

app_name = 'secondapp'

urlpatterns = [
    path('first2/', first2, name = 'first2'),
    path('second2/', second2, name = 'second2'),
    path('third2/', third2, name = 'third2'),
]