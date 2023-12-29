import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.verification_key = ''.join([str(random.randint(0, 9)) for _ in range(15)])
        new_user.save()
        send_mail(
            subject='Hello, little friend',
            message=f'You\'ve been registered, to verify your email, follow that link: '
                    f'http://127.0.0.1:8000/users/verify/{new_user.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Password changed',
        message=f'You requested a new password, so we did it for you, here it is: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))


def verify_user_mail(request, uid):
    for user in User.objects.all():
        if user.verification_key == uid:
            user.is_active = True
            user.save()
            return redirect(reverse('catalog:home'))
    return redirect(reverse('catalog:home'))
