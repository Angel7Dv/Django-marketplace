from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.forms import ModelForm

from apps.product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']



class CustomCreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']


