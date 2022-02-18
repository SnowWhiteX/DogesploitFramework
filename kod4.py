import requests
knk=input("enter url : ")
qwe=requests.get(knk,verify=False)
fayil=open("index.html","w")
fayil.write(str(qwe.content))
fayil.close()
