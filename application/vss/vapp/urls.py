from django.urls import path
from . import views

app_name = 'vapp'
urlpatterns = [
    path("", views.index, name='index'),
    path('encrypt/', views.encrypt, name="encrypt"),
    path('verify/', views.verify, name="verify"),
    path('decrypt/', views.decrypt, name="decrypt"),
]
