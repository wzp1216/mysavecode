import json
import requests
import http.client, urllib


def json_dayenglish():
    resp=requests.get("http://api.tianapi.com/everyday/index?key=e44c6978de6908de52862597c7aed92e&num=10")
    data1=json.loads(resp.text)
    for ddd in data1['newslist']:
        print(ddd['content'])
        print(ddd['note'])

def json_hot():
    conn = http.client.HTTPSConnection('api.tianapi.com') 
    params = urllib.parse.urlencode({'key':'e44c6978de6908de52862597c7aed92e'})
    headers = {'Content-type':'application/x-www-form-urlencoded'}
    conn.request('POST','/networkhot/index',params,headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode('utf-8'))
    print('----------------------------------')
    resp=requests.get("http://api.tianapi.com/everyday/index?key=e44c6978de6908de52862597c7aed92e&num=10")
    dict1=resp.json()
    news=dict1['newslist']
    for new in news:
        print(new)
    print('----------------------------------')

def getjoke():
    conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
    params = urllib.parse.urlencode({'key':'e44c6978de6908de52862597c7aed92e','num':'10'})
    headers = {'Content-type':'application/x-www-form-urlencoded'}
    conn.request('POST','/joke/index',params,headers)
    res = conn.getresponse()
    print(type(res))
    data = res.read()

    print(type(data))

    print('----------------------------------')



if __name__=='__main__':
    print('start----------------------------------')
    json_dayenglish()
    getjoke()
    print('end----------------------------------')


