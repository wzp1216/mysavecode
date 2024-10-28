
#encoding =utf-8

def funinfinite(**kwargs):
  for key,value in kwargs.items():
    print(f"key:{key},value={value}")




if __name__=="__main__":
  funinfinite(a=1,b=2)
