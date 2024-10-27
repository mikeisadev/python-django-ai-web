from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import User

# Create your views here.
def index(request):
    users = User.objects.order_by('-registration_date')

    ctx = {
    'users': users
    }  

    return render(request, 'aitools/index.html', ctx)

def view_document(request):
    
    return HttpResponse('documento')