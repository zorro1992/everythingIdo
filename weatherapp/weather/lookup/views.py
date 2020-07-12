from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=88901&distance=25&API_KEY=FFA2B9D6-A8A1-437C-BD71-331FF837FDC8")

    try:
        api = json.loads(api_request.content)
        
    except Exception as e:
        api = "Error...."


    return render(request,'home.html',{'api': api})

def about(request):
    return render(request,'about.html',{})