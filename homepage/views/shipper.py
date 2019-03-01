from django.conf import settings
from django_mako_plus import view_function, jscontext
import requests

@view_function
def process_request(request):
    r = requests.get('http://148.100.87.242:3000/api/edu.byu.Business/BUSINESS_3')
    r2 = requests.get('http://148.100.87.242:3000/api/edu.byu.Animal')

    context = {
        "incoming": r.json(),
        "current": r2.json()
    }
    return request.dmp.render('shipper.html', context)

@view_function
def receiveproduct(request):

    url = "http://148.100.87.242:3000/api/edu.byu.AnimalMovementArrival"

    payload = "animal=ANIMAL_1&to=BUS_SHIPPER_1&from=BUS_MANUFACTURER_1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "787a1e29-44e1-4ffe-95ec-8d308c9a8812"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

# def receive_asset():
'''
marks asset as received, gives shipper responsibility of the asset until sent
'''

# def send_asset():
'''
marks asset as sent, clears shipper of responsibility of the asset until received by a distributor or retailer
'''