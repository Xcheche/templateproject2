from django.shortcuts import render
from django.http import HttpResponse
import datetime


def wish(request):
    date = datetime.datetime.now()
    h = date.strftime("%H")
    msg = "Hello Guest !!! Very Good"
    if int(h) < 12:
        msg = msg + " Morning !!"
    elif int(h) < 16:
        msg = msg + " Afternoon !!"
    else:
        msg = msg + " Evening !!"
    return render(request, 'testapp/wish.html', {'msg': msg, 'date': date})