from accounts.models import Profile
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Autoridad
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "app_general/index.html")


def creditos(request):
    return render(request, "app_general/creditos.html")


def register(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password= user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('index')

    return render(request, "registration/register.html", data)

## ------------------------------------------------------------------------------------------------
@login_required
def detalle_profile(request, id):
    perfil = get_object_or_404(Profile, pk=id)
    form = ProfileForm(instance=perfil)
    return render(request, 'app_general/edit_profile.html', {'form': form})


@login_required
def edit_profile(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'POST':        
        form = ProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=usuario)
    
    context = {'form': form}
    return render(request, 'app_general/edit_profile.html', context)

## ------------------------------------------------------------------------------------------------


def autoridades(request):
    autoridades = Autoridad.objects.all()
    return render(request, "app_general/autoridades.html", {'autoridades': autoridades})


def password_reset_request(request):
    return render(request, 'registration/reset_password.html')


