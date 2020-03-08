from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=0&API_KEY=2570C5B9-E73C-435D-8B6E-CD24B7B2F329")
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=0&API_KEY=2570C5B9-E73C-435D-8B6E-CD24B7B2F329")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api ="Error"

    if api:
        aqi_quality = api[0]['Category']['Name']
        if aqi_quality == "Good":
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif aqi_quality == "Moderate":
            category_description = "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif aqi_quality == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif aqi_quality == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif aqi_quality == "Very Unhealthy":
            category_description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif aqi_quality == "Hazardous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous"
    else:
        api ="Errors"
        category_description = "No data found"
        category_color = "usg"
        
    return render(request, 'home.html',{'api': api,
    'category_description': category_description,
    'category_color': category_color})
   
def about(request):
    return render(request, 'about.html',{})
