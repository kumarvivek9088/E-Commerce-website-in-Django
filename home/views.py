from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
    # homeappliancescategory = Category.objects.filter(name='home appliances')[0]
    # homeappliancescategory = Category.objects.filter(Q(parent_category = homeappliancescategory.id) | Q(name = "home appliances"))
    # homeappliancesproduct = Products.objects.filter(category__in = homeappliancescategory )
    newproducts = Products.objects.all().order_by('-id')[:15]
    electronicscategory = Category.objects.filter(name='electronics')[0]
    electronicscategory = Category.objects.filter(Q(parent_category = electronicscategory.id) | Q(name = 'electronics'))
    electronicsproducts = Products.objects.filter(category__in = electronicscategory)
    kitchencategory = Category.objects.filter(name='kitchen products')[0]
    kitchencategory = Category.objects.filter(Q(name='kitchen products') | Q(parent_category = kitchencategory.id))
    kitchenproducts = Products.objects.filter(category__in = kitchencategory)
    homecategory = Category.objects.filter(name='ac')[0]
    homeappliance = Products.objects.filter(category = homecategory.id)[0]
    grocerycategory = Category.objects.filter(name='grocery')[0]
    groceryproduct = Products.objects.filter(category = grocerycategory.id)[0]
    automotivecategory = Category.objects.filter(name = 'automotive essentials')[0]
    automotiveproduct = Products.objects.filter(category = automotivecategory.id)[0]
    clothescategory = Category.objects.filter(name='clothes')[0]
    clothescategory = Category.objects.filter(Q(name= 'clothes') | Q(parent_category = clothescategory.id))
    clothesproduct = Products.objects.filter(category__in = clothescategory)[0]
    cameracategory = Category.objects.filter(name="camera")[0]
    cameraproduct = Products.objects.filter(category = cameracategory.id)[0]
    gymcategory = Category.objects.filter(name="gym equipment")[0]
    gymproduct = Products.objects.filter(category = gymcategory.id)[0]
    homeessentialscategory = Category.objects.filter(name = "home essentials")[0]
    homeessentialsproduct = Products.objects.filter(category = homeessentialscategory.id)[0]
    data = {
        "Data": [
            {"type":"onecard",
             "onecard_data":[
                 {
                     "text":"Appliances for your home | upto 70% off",
                     "image" : homeappliance.images.image.url
                 },
                 {
                     "text" :" Electronics | upto 50% off",
                     "image" : electronicsproducts[0].images.image.url
                 },
                 {
                     "text": "Grocery | upto 40% off",
                     "image": groceryproduct.images.image.url
                 },
                 {
                     "text" : "Automotive essentials | uptp 50% off",
                     "image" : automotiveproduct.images.image.url
                 }
             ]
             },
            {
                "type" : "listcard",
                "listcard_data" : [
                    {"text" : "New Products",
                     "products" : newproducts
                     }
                ]
            },
            {
                "type" : "listcard",
                "listcard_data" : [
                    {
                        "text" : " Electronics Products",
                        "products" : electronicsproducts
                    }
                ]
            },
            {
                "type" : "onecard",
                "onecard_data" : [
                    {
                        "text" : "upto 50% off | Clothes",
                        "image" : clothesproduct.images.image.url
                    },
                    {
                        "text" : "upto 40% off | Cameras",
                        "image" : cameraproduct.images.image.url
                    },
                    {
                        "text" : "upto 40% off | GYM Products",
                        "image" : gymproduct.images.image.url
                    },
                    {
                        "text" : "upto 50% off | Home essentials",
                        "image" : homeessentialsproduct.images.image.url
                    }
                ]
            },
            {
                "type" : "listcard",
                "listcard_data" : [
                    {
                        "text" : "Kitchen Products",
                        "products" : kitchenproducts
                    }
                ]
            }
        ]
    }
    
    return render(request,"Home.html",context=data)