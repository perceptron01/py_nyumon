import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
city_code = {'city':270000}
whether_data = requests.get(api_url, params=city_code).json()

print(
    whether_data['forecasts'][0]['dateLabel']
     + 'の天気は '
     + whether_data['forecasts'][0]['telop']
     + ' でーす')