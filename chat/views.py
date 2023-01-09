from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request, 'chat/chatPage.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('chat-page')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register_user.html', {'form': form})

def profile_list(request):
    return render(request, 'chat/profile_list.html')

