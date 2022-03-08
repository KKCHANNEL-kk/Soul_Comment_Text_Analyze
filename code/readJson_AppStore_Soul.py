# encoding:utf-8

import json
import pandas as pd

df = pd.DataFrame(columns=('title','content','rating','version','votecount','votesum','time','page'))
for index in range(10):
    with open('data/AppStore_Soul/page{:d}.json'.format(index+1),'r', encoding='utf-8') as f:
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
        
df.to_csv('data/allcontent_AppStore_Soul.csv',encoding='utf-8-sig',index=None)