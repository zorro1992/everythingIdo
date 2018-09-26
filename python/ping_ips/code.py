# This code reads a json in the same dir and then makes it a dic . From there we pic only the keys and we ping the servers. 

import json
import os
ip_list= []
with open('ip.json') as data:
    data_1 = json.load(data)
    ip_list = [x['ip'] for x in data_1]

print(ip_list)

for x in ip_list:
    response = os.system("ping -c 1 " + x)
    if response == 0:
        print (x, 'is up!')
    else:
        print (x, 'is down!')
