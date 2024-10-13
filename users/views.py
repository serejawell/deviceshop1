import secrets

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config import settings
from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Welcome to the Secret Shop!',
            message=
            f'''Hello, {user.first_name} {user.last_name}!
            Thank you for registering!
            Link for confirm email: {url}''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class CustomLoginView(LoginView):
    form_class = UserLoginForm  # Указываем вашу форму
    template_name = 'users/login.html'  # Шаблон для страницы входа (путь можно изменить)