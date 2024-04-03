import requests
from django import template
from ip2geotools.databases.noncommercial import DbIpCity
#from geopy.distance import distance

register = template.Library()

@register.simple_tag
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    # print(response)
    return response["ip"]

@register.simple_tag
def get_tracker_location():
    res = DbIpCity.get(get_ip(), api_key="free")
    #print(res.ip_address + " -> " + res.region)
    return res.region