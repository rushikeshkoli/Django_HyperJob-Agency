from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.http import HttpResponse
# Create your views here.


class ResumesView(View):

    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, 'resumes.html', context={'resumes': resumes})


class AddResume(View):

    def post(self, request):
        user = request.user
        if user.is_authenticated and not user.is_staff:
            Resume.objects.create(
                description=request.POST.get('description'),
                author=user
            )
            return redirect('/home')
        else:
            return HttpResponse(status=403)
