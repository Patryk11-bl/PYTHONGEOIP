import geocoder
import folium

def get_localization(ip_addr):
    location = geocoder.ip(ip_addr)
    return location

myip  = input('Wprowadź adres ip do zlokalizowania')
location_info = get_localization(myip)

print('country', location_info.country)
print('city', location_info.city)
print('latitude, longitude', location_info.latlng[0], location_info.latlng[1])

coordinate = [location_info.latlng[0], location_info.latlng[1]]
myloc = folium.Map(location=coordinate, zoom_start=14, popup='My Location')
folium.Marker(coordinate, icon=folium.Icon(color='blue', icon_color='blue', prefix='fa',icon='male')).add_to(myloc)
folium.Circle(location=coordinate, radius=200).add_to(myloc)
myloc.save('mymap.html')

