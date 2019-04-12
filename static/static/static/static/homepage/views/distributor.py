from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {
        
    }
    return request.dmp.render('distributor.html', context)

# def receive_asset():
'''
receives asset from shipper
gives responsibility of asset to the distributor
removes responsibility from the shipper
'''

# def process_asset():
'''
transforms asset into one that can be sold by a retailer
'''

# def send_asset():
'''
sends asset to shipper to then be sold at a retailer
removes responsibility of asset from the distributor
gives responsibility of asset to the shipper
'''