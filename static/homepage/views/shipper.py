from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {
        
    }
    return request.dmp.render('shipper.html', context)

# def receive_asset():
'''
marks asset as received, gives shipper responsibility of the asset until sent
'''

# def send_asset():
'''
marks asset as sent, clears shipper of responsibility of the asset until received by a distributor or retailer
'''