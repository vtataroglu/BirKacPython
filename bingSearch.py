#pip install py-bing-search
#Blog Yazisi : http://bit.ly/1iEZHZt

from py_bing_search import PyBingSearch

file = open("siteurl.txt", "wb")

bing = PyBingSearch('API-KEY')
result_list, next_uri = bing.search("Sorgu Cümleciği", limit=50, format='json')

for result in result_list:
    file.write(result.url+"\n");

file.close()
