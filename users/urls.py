from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from users.apps import UsersConfig
from users.views import RegisterView, CustomLoginView, email_verification, ProfileUpdateView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
