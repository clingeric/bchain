from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {
        
    }
    return request.dmp.render('create.html', context)

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
