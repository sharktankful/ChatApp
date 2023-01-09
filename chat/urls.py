from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # Main Chat Page
    path('', chat_views.chatPage, name='chat-page'),

    # Login-section
    path('auth/login/', LoginView.as_view(template_name='chat/LoginPage.html'), name='login-user'),
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),

    # Register-section
    path('register/', chat_views.register_user, name='register'),

    # Profile List
    path('profile_list/', chat_views.profile_list, name='profile-list')
]
