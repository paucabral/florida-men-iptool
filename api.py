from requests import get
import json

#Lists of keys to be used as the json is returned, to return a dictionary
usedFields = ['ip', 'version', 'country', 'region', 'postal', 'country',
              'timezone', 'country_calling_code', 'asn', 'org', 'latitude', 'longitude']    #Keys for success call
errorFields = ['ip', "error", 'reason']                                                     #Keys for IP error (Invalid IP/ Reserved IP)
rateLimitedFields = ['error', 'reason', 'message']                                          #Keys when API returns rate limited


#Function for API call (specific IP input)
def getSpecificIP(IPAdd):
    urlGet = get("http://ipapi.co/{}/json/".format(IPAdd))
    dicUrl = urlGet.json()

    if 'error' not in dicUrl:   # If no errors are found, return dictionary with elements from usedFields as keys
        filterDic = {item: dicUrl[item] for item in usedFields}
        return filterDic

    elif "error" in dicUrl:  # If rate-limited, just return that.
        return dicUrl

    else:                   # If errors found, return dictionary with elements from errorFields as keys
        errorDic = {item: dicUrl[item] for item in errorFields}
        return errorDic


#Function for API call (autodetect host IP)
def getOwnIP():
    urlGet = get("https://ipapi.co/json")
    dicUrl = urlGet.json()

    # This also requires handling on rateLimited as well.
    if "error" not in dicUrl:
        filterDic = {item: dicUrl[item] for item in usedFields}
        return filterDic

    elif "error" in dicUrl:  # If rate-limited, just return that.
        return dicUrl

    else:                   # If errors found, also return elements from errorFields as keys
        errorDic = {item: dicUrl[item] for item in errorFields}
        return errorDic
