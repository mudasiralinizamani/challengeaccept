# importing the requests library 
import requests 
from pprint import pp, pprint


# api-endpoint 
URL = "https://api.unsplash.com/search/photos?page=3&query=office&client_id=lnPkBSQSyC6A1er9rhw3u01QwDhej9JS2JLkUgAA1Uc"


# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL)
  
# extracting data in json format 
data = r.json() 


  
  
# printing the output 

pprint(data.get('results'))

