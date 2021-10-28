from flask import Flask, redirect, url_for, render_template, request
from api import errorFields, getSpecificIP, getOwnIP, rateLimitedFields
from typing import Any, Dict, Union
import os

app = Flask(__name__, template_folder='.')

# ! This function handles both home() and searchIP() into one function.
def ip_query(given_ip: Union[None, str]) -> Dict[str, Any]:
    assert type(given_ip) is str or given_ip is None, "The given IP is not a string! This is an error."

    # Assumes that given_ip has length.
    req_ip_data = getOwnIP() if not given_ip else getSpecificIP(given_ip)

    # Ensure that the given response doesn't contain fields declared under `errorFields` and `rateLimitedFields`.
    return {
        "address": req_ip_data.get("ip", None),
        "version": req_ip_data.get("version", None),
        "region": req_ip_data.get("region", None),
        "postal_code": req_ip_data.get("postal", None),
        "country": req_ip_data.get("country", None),
        "timezone": req_ip_data.get("timezone", None),
        "calling_code": req_ip_data.get("country_calling_code", None),
        "asn": req_ip_data.get("asn", None),
        "isp": req_ip_data.get("org", None),
        "lat": req_ip_data.get("latitude", None),
        "lng": req_ip_data.get("longitude", None),

    } if "error" not in req_ip_data.keys() else {
        "error": req_ip_data.get("error", None),
        "reason": req_ip_data.get("reason", None)
    }


@app.route("/", methods=['GET'])
def home():
    fetched_data = ip_query(None)

    if "error" in fetched_data.keys():
        return render_template('index.html', error=fetched_data["error"], reason=fetched_data["reason"])

    else:
        return render_template('index.html',
                               ip_address=fetched_data["address"],
                               ip_version=fetched_data["version"],
                               ip_region=fetched_data["region"],
                               ip_postal_code=fetched_data["postal_code"],
                               ip_country=fetched_data["country"],
                               ip_timezone=fetched_data["timezone"],
                               ip_calling_code=fetched_data["calling_code"],
                               ip_asn=fetched_data["asn"],
                               ip_isp=fetched_data["isp"],
                               ip_lat=fetched_data["lat"],
                               ip_lng=fetched_data["lng"],
                               )


@app.route("/", methods=['POST'])
def searchIP():
    ip_address = request.form.get('ip_address')
    fetched_data = ip_query(ip_address)

    if "error" in fetched_data.keys():
        return render_template('index.html', error=fetched_data["error"], reason=fetched_data["reason"])

    else:
        return render_template('index.html',
                               ip_address=fetched_data["address"],
                               ip_version=fetched_data["version"],
                               ip_region=fetched_data["region"],
                               ip_postal_code=fetched_data["postal_code"],
                               ip_country=fetched_data["country"],
                               ip_timezone=fetched_data["timezone"],
                               ip_calling_code=fetched_data["calling_code"],
                               ip_asn=fetched_data["asn"],
                               ip_isp=fetched_data["isp"],
                               ip_lat=fetched_data["lat"],
                               ip_lng=fetched_data["lng"],
                               )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
