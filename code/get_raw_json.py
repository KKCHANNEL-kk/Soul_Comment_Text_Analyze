# encoding:utf-8

import requests
import json

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''

def main():
    count = 0
    for i in range(10):
        i = i + 1
        url = 'https://itunes.apple.com/rss/customerreviews/page=' + str(i) + '/id=1032287195/sortby=mostrecent/json?l=en&&cc=cn'
        r = requests.get(url)
        jsonData = json.loads(r.text)
        with open('data/AppStore_Soul/page{:d}.json'.format(i),'w',encoding='utf-8') as f:
            f.write(json.dumps(jsonData,ensure_ascii=False))
            
        count = count + 1
        print("\r当前进度: {:.2f}%".format(count * 100 / 10), end="")

if __name__ == '__main__':
    main()