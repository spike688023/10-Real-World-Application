import time
from datetime import datetime as dt

hosts_temp=r"/Users/nickboy/Udemy/10-Real-World-Application/App3_Website_blocker/hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]
#website_list=["www.facebook.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    #print(line)
                    #print(any(website in line for website in website_list))
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
