from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, AddressForm
from .models import User, Address
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid credentials"
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    addresses = request.user.addresses.all()
    return render(request, 'accounts/profile.html', {'addresses': addresses})

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            if address.is_default:
                # Remove default from other addresses
                Address.objects.filter(user=request.user, is_default=True).update(is_default=False)
            address.save()
            return redirect('accounts:profile')
    else:
        form = AddressForm()
    return render(request, 'accounts/add_address.html', {'form': form})
