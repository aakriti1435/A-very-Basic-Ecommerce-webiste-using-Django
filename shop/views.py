from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil
import json
# from django.views.decorators.csrf import csrf_exempt
# from paytm import Checksum

# MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';

# Create your views here.


def index(request):
    #return HttpResponse("This is shop")
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides':nSlides,'range':range(1,nSlides), 'product':products}
    #allProds = [[products, range(1,nSlides), nSlides],[products, range(1,nSlides), nSlides]]
    
    allProds=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)

def searchMatch(query, item):
    #return true only if query matches the item
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    else:
        return False
    #To make our search more precise we use tfidVectorizer, or Universal sentence encoder, search word to vec and after converting in vector uh can check sklearn cosine similarity

def search(request):
    #return HttpResponse("search")
    query = request.GET.get('search')

    allProds=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod)!= 0:
            allProds.append([prod, range(1,nSlides), nSlides])

    params = {'allProds': allProds, 'msg':""}
    #print(len(allProds))
    if len(allProds)==0 or len(query)<4:
        params = {'msg':"Please make sure you have entered relevant query search"}

    return render(request, "shop/search.html", params)



def about(request):
    #return HttpResponse("about")
    return render(request, "shop/about.html")

def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        #print(name) #testing 
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        #print(name, email, phone, desc)
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()

    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, "shop/tracker.html")


def productView(request, myid):
    #fetching the product using id 
    product = Product.objects.filter(id=myid)
    #print(product)
    return render(request,"shop/prodView.html",{"product":product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mobile = request.POST.get('mobile', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, mobile=mobile, amount=amount)
        order.save();
        # thank = True
        # id = order.order_id
        # #return render(request, "shop/checkout.html", {'thank':thank, 'id':id})
        # # requesting paytm to transfer the amount to your account after payment is done by the user
        # param_dict = {
        #     'MID':'WorldP64425807474247',  #our merchant id will come here
        #     'ORDER_ID': str(order.order_id),
        #     'TXN_AMOUNT': str(amount) ,
        #     'CUST_ID': email ,
        #     'INDUSTRY_TYPE_ID':'Retail',
        #     'WEBSITE':'WEBSTAGING', #for testing
        #     'CHANNEL_ID':'WEB',
	    #     'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        # }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY )
        return render(request, "shop/paytm.html", {'param_dict':param_dict})


    return render(request, "shop/checkout.html")

#to make payment gateway working you need a merchant account, Merchant id and merchant key

# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'shop/paymentstatus.html', {'response': response_dict})

#     #return HttpResponse('paymnet done')