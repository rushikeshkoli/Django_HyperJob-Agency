from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.http import HttpResponse
# Create your views here.


class VacancyView(View):

    def get(self, request):
        data = Vacancy.objects.all()
        return render(request, 'vacancies.html', context={'vacancy': data})


class AddVacancy(View):

    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_staff:
            Vacancy.objects.create(
                description=request.POST.get('description'),
                author=user
            )
            return redirect('/home')
        else:
            return HttpResponse(status=403)