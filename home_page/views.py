from django.shortcuts import render
from ipware import get_client_ip
from visitors_manager.models import Visitors
from ip2geotools.databases.noncommercial import DbIpCity
# Create your views here.


def home(request):

    
    Ip,is_routable = get_client_ip(request)
    country = ''
    times = 0
    if Ip is None:
        Ip = '0.0.0.0'
    else:
        try:
            response = DbIpCity.get(Ip,api_key="free")
            country = response.country + ','+response.city
        except:
            country = 'Unknown'
    visitor = Visitors.objects.filter(ip = Ip).first()
    print(visitor)
    if visitor:
        visitor.no_visits += 1
    else:            
        visitor = Visitors(ip = Ip,location = country,no_visits = 1)    
    visitor.save() 
    return render(request,'homepage/index.html')