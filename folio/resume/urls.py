from django.urls import path
from .views import resume_page

urlpatterns = [
    path('', resume_page, name='resume_page'),
]
