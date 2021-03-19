import requests
import json
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
def fuzz():
    dom=input("Enter Domain >> ")
    url="https://sonar.omnisint.io/subdomains/"+dom
    r=requests.get(url)
    print(C+"Enumerating Subdomains ^-^ .....")
    for i in r.json():
        print(i)
    print(G+"Subdomain Enumeration Success")
    
if __name__=="__main__":
    fuzz()