from django.urls import path
from .views import usuario, register
 
urlpatterns = [
    #path('', usuario, name='usuario' ),
    path('', register, name='register' ),
]