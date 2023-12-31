import xmlrpc.client

url = "http://localhost:8069"
db = "dev01"
username = '56172@etu.he2b.be'
password = "odoo"

common = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/common'.format(url)
)

print("Version : ", common.version())

uid = common.authenticate(db, username, password, {})
if uid:
    print("********************** CONNECTED **************************")
else:
    print("********************** DISCONNECTED **************************")

models = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/object'.format(url)
)
hasRightApart = models.execute_kw(db, uid, password, 'apartment.sell', 'check_access_rights', [
    'read'], {'raise_exception': False})
hasRightProduct = models.execute_kw(db, uid, password, 'product.template', 'check_access_rights', [
    'read'], {'raise_exception': False})

if hasRightProduct & hasRightApart:
    askSearch = input("Do you want to search apartment ? Yes/No \n")
    Search = False
    if askSearch.upper() == 'YES':
        Search = True
    while (Search):
        apartmentSearch = input(
            "Type name of the apartment you want to search \n")
        apartment = models.execute_kw(db, uid, password, 'apartment.sell', 'search_read', [
            [('name', '=', apartmentSearch)]])
        product = models.execute_kw(db, uid, password, 'product.template', 'search_read', [
            [('idApart', '=', apartmentSearch)]])
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
            askSearch = input("Do you want to search apartment ? Yes/No \n")
            if askSearch.upper() == 'NO':
                Search = False
        else:
            print("No apartment available with this name")
    else:
        print("You need to enter Yes or No")

if hasRightApart == False:
    print("You don't have access to Apartment")

if hasRightProduct == False:
    print("You don't have access to Product")

