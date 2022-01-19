from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login  # Register User and login

# Create your views here.
from .form import CustomCreateUserForm       # Register User
from .models import Posteador          # Register User

from django.contrib.auth.decorators import login_required   # LOGIN


def register(request):		
    if request.method == 'POST':
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():            
            user = form.save()          
            login(request, user)    
            username = form.cleaned_data.get('username')
            Posteador.objects.create(nombre=username, created_by=user)   #[1]Variable para ser usada en el login    
            return redirect('userPanel')
    else:
        form = CustomCreateUserForm()

    ctx = {'form':form}
    return render(request, 'usuarios/register.html', ctx)


@login_required
def userPanel(request): 
    #print("=========",request.user.posteador)
    poster = request.user.posteador  # Variable del model Posteador create_by
    productos = poster.products.all()

    ctx = {
        "usuario": poster,
        "productos": productos
    }
    return render(request, 'usuarios/userPanel.html', ctx)


from .form import ProductForm
from django.utils.text import slugify

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            # pasos necesarios para los formularios con clave primaria
            product = form.save(commit=False)# evita que mande el formulario a la bae de datos ya que faltan los siguientes campos
            product.vendor = request.user.posteador
            product.slug = slugify(product.title) # crea una url a partir de el titulo
            product.save()

            return redirect('userPanel')
    else:
        form = ProductForm()
        print( "Validaciones =", request.method ,form.is_valid() ,form.errors.values())
        
    
    return render(request, 'usuarios/add_product.html', {'form': form})
