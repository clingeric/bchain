from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {
        
    }
    return request.dmp.render('manufacturer.html', context)

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