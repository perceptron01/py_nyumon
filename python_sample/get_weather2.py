import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params = payload).json()
print(weather_data['forecasts'][0]['dateLabel'] + 'の天気は、' + weather_data['forecasts'][0]['telop'])
print(weather_data['forecasts'][1]['dateLabel'] + 'の天気は、' + weather_data['forecasts'][1]['telop'])
print(weather_data['forecasts'][2]['dateLabel'] + 'の天気は、' + weather_data['forecasts'][2]['telop'])
