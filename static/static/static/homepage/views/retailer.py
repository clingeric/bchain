from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    context = {
        
    }
    return request.dmp.render('retailer.html', context)

# def receive_asset():
'''
marks asset as received, gives retailer responsibility of the asset until sold
'''

# def sell_asset():
'''
marks asset as sold, clears retailer of responsibility of the asset
blockchain no longer tracks this asset
'''