from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime
from django.contrib import messages
import time
from home.engines.cron_update import *

from home.models import Accounts

'CRON JOB'


def cron_calls(request):
    manage_update(Accounts)
    return HttpResponse('Cron Called')


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def handle_register(request):
    # insertion logic
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        genre = request.POST.get('genre')
        print(name, username, email, genre)
        account = Accounts(name=name, insta_username=username, email=email, genre=genre, date=datetime.today())
        print("data", Accounts.objects.all()[0].name)
        # cron_calls()
        account.save()
        messages.success(request, 'Query Successful')
        # time.sleep(10)

    return index(request)
