from django.urls import path
from t1 import views

urlpatterns = [
path('',views.home),
path('course/',views.course),
path('about-us/',views.about),
]