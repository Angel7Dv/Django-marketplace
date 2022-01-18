from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login  # Register User and login
from .form import CreateUserForm       # Register User
from .models import Posteador          # Register User

from django.contrib.auth.decorators import login_required   # LOGIN


def register(request):		
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            user = form.save()          
            login(request, user)    
            username = form.cleaned_data.get('username')
            Posteador.objects.create(nombre=username, created_by=user)   #[1]Variable para ser usada en el login    
            return redirect('home')
    else:
        form = CreateUserForm()
    ctx = {'form':form}
    return render(request, 'usuarios/register.html', ctx)


@login_required
def userPanel(request): 
    #print("=========",request.user.posteador)
    poster = request.user.posteador  # Variable del model Posteador create_by
    ctx = {
        "usuario": poster
    }

    return render(request, 'usuarios/userPanel.html', ctx)