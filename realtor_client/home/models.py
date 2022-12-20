from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import xmlrpc.client

class OdooUser(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    odoo_id = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

    # REQUIRED_FIELDS=['first_name', 'last_name', 'email'] 



def authenticate(request):
    url = "http://localhost:8069"
    db = "dev01"
    common = xmlrpc.client.ServerProxy(
        '{}/xmlrpc/2/common'.format(url)
    )   
    print(request)
    username = request.POST['email']
    password = request.POST['password']
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/object'.format(url)
    )
    hasRightApart = models.execute_kw(db, uid, password, 'apartment.sell', 'check_access_rights', [
    'read'], {'raise_exception': False})
    hasRightProduct = models.execute_kw(db, uid, password, 'product.template', 'check_access_rights', [
    'read'], {'raise_exception': False})
    if uid:
        print("LETSSSSSSS GOOOOOOOOOOOOOOOOOOOOOOOOO")

        print(uid)
        if hasRightProduct & hasRightApart:
            apartment = models.execute_kw(db, uid, password, 'apartment.sell', 'search_read', [[('name', '=', 'Apartment 4')]])
            product = models.execute_kw(db, uid, password, 'product.template', 'search_read', [[('idApart', '=', 'Apartment 4')]])
            if len(apartment) > 0:
                print(apartment[0]['name'])
                print(apartment[0]['availability'])
                print(apartment[0]['description'])
                print(apartment[0]['price'])
                print(apartment[0]['apartment_surface'])
                print(apartment[0]['terrace_surface'])
                print(apartment[0]['total_surface'])
                print(apartment[0]['best_offerer'])
                print(apartment[0]['best_price_offer'])
                if len(product) > 0:
                    print(product[0]['qty_available'])
                else:
                    print("No product available")
        return HttpResponseRedirect("/")
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