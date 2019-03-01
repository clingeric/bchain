from django.conf import settings
from django_mako_plus import view_function, jscontext
import requests

@view_function
def process_request(request):
    r = requests.get('http://148.100.87.242:3000/api/edu.byu.Business/BUS_MANUFACTURER_1')
    r2 = requests.get('http://148.100.87.242:3000/api/edu.byu.Animal')

    context = {
        "incoming": r.json(),
        "current": r2.json()
    }
    return request.dmp.render('manufacturer.html', context)

@view_function
def receiveproduct(request):

    url = "http://148.100.87.242:3000/api/edu.byu.AnimalMovementArrival"

    payload = "animal=ANIMAL_1&to=BUS_MANUFACTURER_1&from=BUS_PRODUCER_1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "d5b9772c-8e22-4bbf-929d-4774a216c101"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

@view_function
def sendproduct(request):

    
    url = "http://148.100.87.242:3000/api/edu.byu.AnimalMovementDeparture"

    payload = "animal=ANIMAL_1&from=BUS_MANUFACTURER_1&to=BUS_SHIPPER_1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "3459f746-9891-4158-8062-e3c23caaf6b7"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

# def receive_asset():
'''
receives asset from the producer
clears the producer of the responsibility of the asset
gives the manufacturer responsibility of the asset
'''

# def process_asset():
'''
transforms the raw asset into a sellable one
assigns quality to the asset
'''

# def send_asset():
'''
sends asset off to a shipper
removes responsibility from the manufacturer
gives responsibility to the shipper
'''