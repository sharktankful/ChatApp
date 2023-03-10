from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from chat.forms import SignUpForm

# Create your views here.
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request, 'chat/chatPage.html', context)

def test(request):
    return render(request, 'chat/test-chat.html')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('chat-page')
    else:
        form = SignUpForm()
    return render(request, 'chat/register_user.html', {'form': form})

def profilePage(request):
    return render(request, 'chat/profilePage.html')

# def EditProfilePage(request):
#     return render(request, 'chat/editProfile.html')


