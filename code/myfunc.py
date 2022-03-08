# encoding:utf-8

import requests
import json
import pandas as pd
import os

def getAppStoreReview(appid,filepath):
    count = 0
    if(os.path.exists(filepath)==False):
        os.mkdir(filepath)
        
    for i in range(10):
        i = i + 1
        url = 'https://itunes.apple.com/rss/customerreviews/page=' + str(i) + '/id='+appid+'/sortby=mostrecent/json?l=en&&cc=cn'
        r = requests.get(url)
        jsonData = json.loads(r.text)
        with open(filepath+'/page{:d}.json'.format(i),'w',encoding='utf-8') as f:
            f.write(json.dumps(jsonData,ensure_ascii=False))
            
        count = count + 1
        print("\r当前进度: {:.2f}%".format(count * 100 / 10), end="")

def reviewJson2Csv(appname,filepath):
    df = pd.DataFrame(columns=('title','content','rating','version','votecount','votesum','time','page'))
    for index in range(10):
        with open(filepath+'/page{:d}.json'.format(index+1),'r', encoding='utf-8') as f:
            jsonData = json.load(f)
        
        for entry in jsonData['feed']['entry']:
            row = {'title':entry['title']['label'],
                'content':entry['content']['label'],
                'rating':entry['im:rating']['label'],
                'version':entry['im:version']['label'],
                'votecount':entry['im:voteCount']['label'],
                'votesum':entry['im:voteSum']['label'],
                'time':entry['updated']['label'],
                'page':index+1
                }
            rowdf = pd.DataFrame.from_dict(row,orient='index').T
            df = df.append(rowdf,ignore_index=True)
            
    df.to_csv(filepath+'/allcontent_AppStore_'+appname+'.csv',encoding='utf-8-sig',index=None)