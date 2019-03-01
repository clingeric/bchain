from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
import requests

@view_function
def process_request(request):

    r = requests.get('http://148.100.87.242:3000/api/edu.byu.Animal')

    context = {
        "data": r.json()
    }
    return request.dmp.render('view.html', context)

@view_function
def sendproduct(request):

    url = "http://148.100.87.242:3000/api/edu.byu.AnimalMovementDeparture"

    payload = "animal=ANIMAL_1&from=BUS_PRODUCER_1&to=BUS_MANUFACTURER_1"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return HttpResponseRedirect('/manufacturer')






# def create_asset():
'''
the initial entry into the blockchain of the asset
adds all the necessary info about the asset
'''

# def send_asset():
'''
sends the asset off to the manufacturer, not using any shipper
removes responsibility of the asset from the producer
gives responsibility to the manufacturer
'''
