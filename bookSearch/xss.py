from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myMap")
location = geolocator.geocode("SH12A, Siliguri, Darjiling, Darjeeling, West Bengal, 734005, भारत")
#location = geolocator.reverse("26.7067287,88.4165525")
print(location.address)
print(location.latitude, location.longitude)
#18.6068601,73.872988

# import folium package 
#import folium 
  
# Map method of folium return Map object 
  
# Here we pass coordinates of Gfg  
# and starting Zoom level = 12 
#my_map1 = folium.Map(location = [28.5011226, 77.4099794], 
                                        #zoom_start = 12 ) 
  
# save method of Map object will create a map 
#my_map1.save(" my_map1.html " )  
                                        
# import folium package 
#import folium 
  
#my_map3 = folium.Map(location = [18.6068601, 73.872988], 
 #                                       zoom_start = 15) 

#my_map3 = folium.Map(location = [18.5613223, 73.9149866], 
 #                                       zoom_start = 15) 
  
# Pass a string in popup parameter 
#folium.Marker([18.6068601, 73.872988], 
  #             popup = ' Geeksforgeeks.org ').add_to(my_map3) 
#folium.Marker([18.5613223, 73.9149866], 
   #            popup = ' Geeksforgeeks.org ').add_to(my_map3) 
  
  
#my_map3.save(" my_map3.html ") 
