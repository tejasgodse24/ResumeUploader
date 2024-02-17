from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from myapp.forms import *

# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        context = {
            'form' : form,
            'candidates' : candidates,
        }
        return render(request, 'index.html', context)
    

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        print("hoe")
        if form.is_valid():
            form.save()
        else:
            return render(request, 'index.html', {'form' : form})
        return HttpResponseRedirect(request.path_info)
    


def show_candidate(request, id):
    candidate = Resume.objects.get(uid = id)
    return render(request, 'candidate.html', {'c' : candidate})

