from django.urls import path
from .views import userPanel, register, add_product
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', register, name='register' ),
    path('panel', userPanel, name='userPanel'),
    path('add-product/', add_product, name='add_product'),


    # Login y logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'), 
]