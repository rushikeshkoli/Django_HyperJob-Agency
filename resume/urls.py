from django.urls import path
from .views import ResumesView
urlpatterns = [
    path('', ResumesView.as_view()),
]