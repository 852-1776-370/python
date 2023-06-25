import phonenumbers
import opencage
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import folium
key ="5045f53341d5481da386889d94158bee"
number=input("enter the number for tracking the location")
check_number = phonenumbers.parse(number)

#check if the PhoneNumber is a valid number
if phonenumbers.is_valid_number(check_number):
    print('Given phone number is valid.')
    print(check_number)
else:
    print('Given phone number is not valid.')
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)
# timezone  = timezone.time_zones_for_number(number)
# print(timezone)
service_provider=phonenumbers.parse(number)
provider_name=carrier.name_for_number(service_provider, "en")
print(provider_name)
geocoder = OpenCageGeocode(key)
Query =str(number_location)
request = geocoder.geocode(Query)
lat=request[0]["geometry"]['lat']
lng=request[0]['geometry']['lng']
print(lat,lng)
map_location = folium.Map(location=[lat,lng], zoom_start=9 )
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("map_location.html")
