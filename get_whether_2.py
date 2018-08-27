import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
city_code = {'city':270000}
whether_data = requests.get(api_url, params=city_code).json()

for whether in whether_data['forecasts']:
    print(
        whether['dateLabel']
        + 'の天気は '
        + whether['telop']
        + ' でーす')
print(whether)