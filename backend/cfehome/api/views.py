import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view #
from django.http import JsonResponse, HttpResponse
from products.models import Product 
from products.serializers import ProductSerializer
# Create your views here.
#API VIEW 

@api_view(["GET"])
def api_home(request, *args, **kwargs):

    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data={}
    if instance:
       #data = model_to_dict(instance)  #model to dictionnary
       #print(type(data) ,"views data")
       data = ProductSerializer(instance).data 
    return JsonResponse(data)  
   
    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    """ first part (youtube: ): 
    # request -> Httprequest -> Django
    # print Dir(request)
    # request.body 
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of Json data --> Python Dict
    except: 
        pass
    print(data, "print data from api")
    data['headers'] = request.headers #request.META -->
    print(request.headers , 'this is headers')
    data['content_type'] = request.content_type

    return JsonResponse({"message" : "hi there, this is your django api response!!"})"""




