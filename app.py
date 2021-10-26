from flask import Flask, redirect, url_for, render_template, request
from api import errorFields, getSpecificIP, getOwnIP, rateLimitedFields
from typing import Any, Dict, Union
import os

app = Flask(__name__, template_folder='.')

# ! This function handles both home() and searchIP() into one function.
def ip_query(given_ip: Union[None, str]) -> Dict[str, Any]:
    
    assert type(given_ip) is str or given_ip is None, "The given IP is not a string! This is an error."

    req_ip_data = getOwnIP() if not given_ip else getSpecificIP(given_ip) # Assumes that given_ip has length.

    ip_info = {}

    if req_ip_data: # Check if the variable has a content.
        if list(req_ip_data.keys()) != errorFields and list(req_ip_data.keys()) != rateLimitedFields:
            # Ensure that the given response doesn't contain fields declared under `errorFields` and `rateLimitedFields`.
            ip_info = {
                "address": req_ip_data["ip"],
                "version": req_ip_data["version"],
                "region": req_ip_data["region"],
                "postal_code": req_ip_data["postal"],
                "country": req_ip_data["country"],
                "tz": req_ip_data["timezone"],
                "calling_code": req_ip_data["country_calling_code"],
                "asn": req_ip_data["asn"],
                "isp": req_ip_data["org"],
                "lat": req_ip_data["latitude"],
                "lng": req_ip_data["longitude"]
            }
        

    else: # Evaluates to None. Map other errors for rate-limited and actual error given data. 
        ip_info = {
            "error": req_ip_data["ip"] if list(req_ip_data.keys()) == errorFields else req_ip_data["reason"],
            "reason": req_ip_data["reason"] if list(req_ip_data.keys()) != errorFields else req_id_data["message"]
        }

    return ip_info

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', ip_context = ip_query(None))


@app.route("/", methods=['POST'])
def searchIP():
    # For test purposes, use "request.json.get()" instead. Error is not handled here.
    # ip_address = request.form.get('ip_address') # Before
    ip_address = request.json.get("ip_address") # After

    return render_template('index.html', ip_context = ip_query(ip_address))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
