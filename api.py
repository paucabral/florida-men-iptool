from requests import get
import json

usedFields = ['ip', 'version', 'country', 'region', 'postal', 'country',
              'timezone', 'country_calling_code', 'asn', 'org', 'latitude', 'longitude']
errorFields = ['ip', "error", 'reason']
rateLimitedFields = ['error', 'reason', 'message']


def getSpecificIP(IPAdd):

    urlGet = get("http://ipapi.co/{}/json/".format(IPAdd))
    dicUrl = urlGet.json()

    if 'error' not in dicUrl:
        filterDic = {item: dicUrl[item] for item in usedFields}
        return filterDic

    elif "error" in dicUrl:  # If rate-limited, just return that.
        return dicUrl

    else:
        errorDic = {item: dicUrl[item] for item in errorFields}
        return errorDic


def getOwnIP():
    urlGet = get("https://ipapi.co/json")
    dicUrl = urlGet.json()

    # This also requires handling on rateLimited as well.
    if "error" not in dicUrl:
        filterDic = {item: dicUrl[item] for item in usedFields}
        return filterDic

    elif "error" in dicUrl:  # If rate-limited, just return that.
        return dicUrl

    else:
        errorDic = {item: dicUrl[item] for item in errorFields}
        return errorDic
