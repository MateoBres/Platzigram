"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


# URLs
    # from platzigram import views as local_views
    # path('hello-world/', local_views.hello_world, name='hello_world'),
    # path('sorted/', local_views.sort_integers, name='sort'),
    # path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'), #PATH-CONVERTER

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]#Capturamos datos engresado por la URL en este caso hi/?numbers=10,4,65,7 y los ponemos en orden
    sorted_ints = sorted(numbers)
    data = { #Creamos un objeto tipo API
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),#traduce un objeto a un Json
        content_type='application/json'
    )

"""Get data from URL.py by PATH-CONVERTER"""
def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)