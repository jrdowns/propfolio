from django.shortcuts import render

# Create your views here.
def resume_page(request):
    return render(request, 'resume/resume_page.html')
