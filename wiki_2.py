import requests, sys

search_word = sys.argv[1]

api_base_url = "https://ja.wikipedia.org/w/api.php"
api_params = {
    'format':'xmlfm', # 'xml',
    'action':'query', 
    'prop':'revisions', 
    'rvprop':'content'}
api_params['titles'] = search_word

wiki_data = requests.get(api_base_url, params = api_params)
file_obj = open('/Users/tanaka_yuki/Documents/02_study/py_nyumon/' + search_word + '.html', 'w')
file_obj.write(wiki_data.text)
file_obj.close()
