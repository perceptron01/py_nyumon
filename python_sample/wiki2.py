import requests, sys
import codecs #Windowsの場合
search_word = sys.argv[1]
api_url = 'https://ja.wikipedia.org/w/api.php'
payload = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
payload['titles'] = search_word
wiki_data = requests.get(api_url, params=payload)
fo = codecs.open('C:\\Users\\aarai.SBCR\\Desktop\\'+ search_word + '.html', 'w', 'utf-8') #Windowsの場合
#fo = open('/Users/（ユーザー名）/Desktop/'+ search_word + '.html', 'w') #Macの場合
fo.write(wiki_data.text)
fo.close()
