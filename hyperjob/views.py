from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User


# Create your views here.


class MenuView(View):
    paths = ['login', 'signup', 'vacancies', 'resumes', 'home']

    def get(self, request):
        my_paths = self.paths.copy()
        if request.user.is_authenticated:
            my_paths = my_paths[2:]
        return render(request, 'index.html', context={'paths': my_paths})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'


class SignOutView(LogoutView):
    next_page = '/'


class UserProfile(View):
    curr_user = ''

    def get(self, request):
        self.curr_user = request.user
        print(self.curr_user.is_staff)
        return render(request, 'userProfile.html', context={'user': self.curr_user,
                                                            'is_staff': self.curr_user.is_staff})
