import json
import requests
import http.client, urllib

def openafile():
    f=None
    try:
        f=open('./test.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("no file found,open error!\n")
    except LookupError:
        print('encode is error')
    except UnicodeDecodeError:
        print('read an encode error')
    finally:
        if f:
            f.close()
def json_write():
    dict1={
            'name':'wzy',
            'age':13,
            'qq':3423421,
            'friends':['li','zhao'],
            'cars':[{'brand':'Benz','maxspeed':330},
                {'brand':'Audi','maxspeed':300},
                {'brand':'porsche','maxspeed':360}]
            }
    try:
        with open('test.json','w',encoding='utf-8') as fs:
            json.dump(dict1,fs)
    except IOError as e:
        print(e)
    print("save the data")

def json1():
    resp=requests.get("http://api.tianapi.com/networkhot/index?key=e44c6978de6908de52862597c7aed92e&num=10")
    data1=json.loads(resp.text)
    for news in data1['newslist']:
        print(news['title'])

def json_dayenglish():
    resp=requests.get("http://api.tianapi.com/everyday/index?key=e44c6978de6908de52862597c7aed92e&num=10")
    data1=json.loads(resp.text)
    for ddd in data1['newslist']:
        print(ddd['content'])
        print(ddd['note'])

def json2():
    conn = http.client.HTTPSConnection('api.tianapi.com') 
    params = urllib.parse.urlencode({'key':'e44c6978de6908de52862597c7aed92e'})
    headers = {'Content-type':'application/x-www-form-urlencoded'}
    conn.request('POST','/networkhot/index',params,headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode('utf-8'))


if __name__=='__main__':
    json_dayenglish()


