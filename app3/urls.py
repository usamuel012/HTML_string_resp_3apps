from django.urls import path
from app3.views import *

app_name = 'thirdapp'

urlpatterns = [
    path('first3/', first3, name = 'first2'),
    path('second3/', second3, name = 'second3'),
    path('third3/', third3, name = 'third3'),
]