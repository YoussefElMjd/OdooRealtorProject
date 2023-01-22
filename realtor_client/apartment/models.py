from django.db import models
from django.http import HttpResponseRedirect
import xmlrpc.client
from django.shortcuts import render

def get_apartment(): 
    allApartment = models.execute_kw(db, uid, passw, 'apartment.sell', 'search_read', [])
    x = range(0, len(allApartment))
    if len(allApartment) > 0:
        for i in x:
                allApartment[i]['best_offerer'] = allApartment[i]['best_offerer'][1]
                product = models.execute_kw(db, uid, passw, 'product.template', 'search_read',
                 [[('idApart', '=', allApartment[i]['name'])]])
                if len(product) > 0:
                    allApartment[i]['qty_available'] = product[0]['qty_available']
                else:
                    allApartment[i]['qty_available'] = 0
        return allApartment

def set_offer(request):
    value = models.execute_kw(db, uid, passw, 'res.partner', 'search_read', [[('name', '=', request.POST["offerer"])]])
    if not value :
        create(request.POST["offerer"])

    if float(request.POST["amount"]) > float(request.POST["best_offer"]):
        offer = get_offer_by_name(request.POST["offerer"])
        models.execute_kw(db, uid, passw, 'apartment.sell','write',[[int(request.POST["apartment"])],
    {'best_offerer' : offer[0]['id'],
    'best_price_offer': int(request.POST["amount"])}])
    else :
        return render(request,'apartment/apartment.html', {'apartments': get_apartment(),'connected' : "True", 
        'error' : "You need to enter an amount above the current best offer " + request.POST["best_offer"], 'apart_offer' : request.POST["apartment"]})
    return render(request,'apartment/apartment.html', {'apartments': get_apartment(),'connected' : "True"})
    
def authenticate(request):
    if(request.POST['connected'] == "False"):
        global user
        global passw
        global uid
        global url
        global db
        global common
        global models
        url = request.POST['url']
        common = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(url)
        )   
        user = request.POST['email']
        passw = request.POST['password']
        db = request.POST['db']
        uid = common.authenticate(db, user, passw, {})
        models = xmlrpc.client.ServerProxy(
        '{}/xmlrpc/2/object'.format(url)
        )
        hasRightApart = models.execute_kw(db, uid, passw, 'apartment.sell', 'check_access_rights', 
        ['read'], {'raise_exception': False})
        hasRightProduct = models.execute_kw(db, uid, passw, 'product.template', 'check_access_rights', 
        ['read'], {'raise_exception': False})
        if uid:
            if(hasRightApart & hasRightProduct):
                allApartment = get_apartment()
                return render(request,'apartment/apartment.html', {'apartments': allApartment})
        else:
                return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/loginAuth")

def create(name):
    models.execute_kw(db,uid,passw, 'res.partner', 'create', [{'name' : name}])

def get_offer_by_name(name):
    return models.execute_kw(db,uid,passw,'res.partner','search_read', [[('name', '=', name)]])