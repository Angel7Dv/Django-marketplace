from django.shortcuts import render, redirect

# Create your views here.
from .models import Posteador                             #Add this for user
from django.contrib.auth import login                   #Add this for user
from .form import CreateUserForm
from django.contrib import messages



def register(request):		
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form            
            #login(request, user)    
            #username = form.cleaned_data.get('username')
            #posteador = Posteador.objects.create(name=username created_by=user)           
            return redirect('home')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'usuarios/register.html', context)



def usuario(request):
    return request(render, 'usuarios,usuario.html')
