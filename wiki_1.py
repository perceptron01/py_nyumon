import requests

api_base_url = "https://ja.wikipedia.org/w/api.php"
api_params = {
    'format':'xmlfm', # 'xml',
    'action':'query', 
    'titles':'安室奈美恵', 
    'prop':'revisions', 
    'rvprop':'content'}
wiki_data = requests.get(api_base_url, params = api_params)
file_obj = open('/Users/tanaka_yuki/Documents/02_study/py_nyumon/wiki_xml.html', 'w')
file_obj.write(wiki_data.text)
file_obj.close()