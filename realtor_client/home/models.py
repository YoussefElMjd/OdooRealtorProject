from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import xmlrpc.client
from django.shortcuts import render

class OdooUser(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    odoo_id = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

    # REQUIRED_FIELDS=['first_name', 'last_name', 'email'] 


url = "http://localhost:8069"
db = "dev01"


def get_apartment(): 
    allApartment = models.execute_kw(db, uid, passw, 'apartment.sell', 'search_read', [])
    x = range(0, len(allApartment))
    if len(allApartment) > 0:
        for i in x:
                # print("\n")
                # print(allApartment[i]['name'])
                # print(allApartment[i]['availability'])
                # print(allApartment[i]['description'])
                # print(allApartment[i]['price'])
                # print(allApartment[i]['apartment_surface'])
                # print(allApartment[i]['terrace_surface'])
                # print(allApartment[i]['total_surface'])
                # print(allApartment[i]['best_offerer'])
                # print(allApartment[i]['best_price_offer'])
                product = models.execute_kw(db, uid, passw, 'product.template', 'search_read', [[('idApart', '=', allApartment[i]['name'])]])
                if len(product) > 0:
                    allApartment[i]['qty_available'] = product[0]['qty_available']
                    print(allApartment[i]['qty_available'])
                    # print(product[0]['qty_available'])
                else:
                    allApartment[i]['qty_available'] = 0
                    print(allApartment[i]['qty_available'])
                    # print("No product available")
        return render('home/apartment.html', {'apartments': allApartment})

def set_offer(request):
    print(user)
    print(passw)
    return HttpResponseRedirect('/')
    
def authenticate(request):
    global user
    global passw
    global uid
    global common
    global models
    common = xmlrpc.client.ServerProxy(
        '{}/xmlrpc/2/common'.format(url)
    )   
    user = request.POST['email']
    passw = request.POST['password']
    uid = common.authenticate(db, user, passw, {})
    models = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/object'.format(url)
    )
    hasRightApart = models.execute_kw(db, uid, passw, 'apartment.sell', 'check_access_rights', [
    'read'], {'raise_exception': False})
    hasRightProduct = models.execute_kw(db, uid, passw, 'product.template', 'check_access_rights', [
    'read'], {'raise_exception': False})
    if uid:
        if(hasRightApart & hasRightProduct):
            print("LETSSSSSSS GOOOOOOOOOOOOOOOOOOOOOOOOO")
            get_apartment()
    else:
        print(" DONT LETSSSSSSS GOOOOOOOOOOOOOOOOOOOOOOOOO")
        return HttpResponseRedirect("/")


def create(request):
    # form = OdooUserForm(request.POST)
    # #if form.is_valid():
	#   #  user = form.save()
    #  #   login(request, user)   
    # odooUser = OdooUser.objects.create(
    #     email=request.POST['email'],
    #     password=request.POST['password'],
    #     )

    return HttpResponseRedirect("/")