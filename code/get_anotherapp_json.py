# encoding:utf-8

import requests
import json
import myfunc

appname = input("appname: ")
appid = input("appid: ")

myfunc.getAppStoreReview(appid,'data/AppStore_'+appname)
myfunc.reviewJson2Csv(appname,'data/AppStore_'+appname)