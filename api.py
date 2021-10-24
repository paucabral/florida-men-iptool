from requests import get
import json

#free account url structure https://ipapi.co/8.8.8.8/json/
# accessKey = 'd44cff8af5f8c516042fcf9b21ea84ce' (for "ipapi.com")
usedFields = ['ip', 'version', 'country', 'region', 'postal', 'country', 'timezone', 'country_calling_code', 'asn', 'org', 'latitude', 'longitude']
errorFields = ['ip', 'reason']

def getSpecificIP(IPAdd):

    urlGet = get("http://ipapi.co/{}/json/".format(IPAdd))
    dicUrl = urlGet.json()
    if 'error' not in dicUrl:      
        filterDic = {item: dicUrl[item] for item in usedFields}
        return filterDic
    else:
        errorDic = {item: dicUrl[item] for item in errorFields}
        return errorDic

def getOwnIP():
    urlGet = get("https://ipapi.co/json")
    dicUrl = urlGet.json()
    filterDic = {item: dicUrl[item] for item in usedFields}
    return filterDic
    

# IP address types:
# 2001:4451:87c5:5b00:6d85:a283:46c7:af40 Own IPv6
# 2.2.2.2 Specific IPv4
# 192.168.0.0 Invalid - Reserved IPv4 
# 172.338.9.32 Invalid IPv4