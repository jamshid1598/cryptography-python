# django
from django.shortcuts import (
    render, 
    redirect,
)
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.urls import reverse_lazy
from django.views import generic

# local files
from .forms import (
    NewUserForm,
)


# Create your views here.






def login_view(request):
    template_name = 'registration/login.html'
    context = {}
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['error'] = "invalid username or password"
        else:
            context['error'] = "invalid username or password"
    form = AuthenticationForm()
    context['form'] = form
    return render(request, template_name, context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    print(request.path)
    return redirect('user:login')


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("user:login")
    template_name = "registration/signup.html"




def signup_view(request):
    template_name = 'registration/signup.html'
    context = {}
    
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            print('working')
            username = form.cleaned_data.get('username')
            # phonenumber = form.cleaned_data.get('phonenumber')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['error'] = "invalid username or password"
        else:
            print(form.errors)
            context['error'] = "invalid username or password"
    form = NewUserForm()
    context['form'] = form
    return render(request, template_name, context)