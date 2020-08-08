"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import MenuView, MyLoginView, SignUpView, LogoutView, UserProfile
from vacancy.views import AddVacancy
from resume.views import AddResume
from django.views.generic import RedirectView
urlpatterns = [
    path('', MenuView.as_view()),
    path('vacancies', include('vacancy.urls')),
    path('resumes', include('resume.urls')),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', SignUpView.as_view()),
    path('vacancy/new', AddVacancy.as_view()),
    path('resume/new', AddResume.as_view()),
    path('home', UserProfile.as_view()),
    path('admin/', admin.site.urls),
]
