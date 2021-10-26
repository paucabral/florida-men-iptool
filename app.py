from flask import Flask, redirect, url_for, render_template, request
from api import errorFields, getSpecificIP, getOwnIP, rateLimitedFields
from typing import Any, Dict, Optional, Union
import os

app = Flask(__name__, template_folder='.')

# ! This function handles both home() and searchIP() into one function.
def ip_query(given_ip: str, meth: Union["GET", "POST"]) -> Dict[str, Any]:
    # Pre-check on given arguments before processing.

    # Asserts
    if meth == "GET":
        assert given_ip is None, "The given method is 'GET' but the callback contains 'given_ip'. This is unintended."

    elif meth == "POST":
        assert given_ip is not None, "The given method is 'POST', but the callback does not contain 'given_ip' This is unintended."
        assert type(given_ip) is str, "The given IP is not a string! This is an error."
    
    else:
        raise ValueError(f"The given method ({meth.upper()}) is not available! Please get to the basic API methods.")

    req_ip_data = getOwnIP() if meth == "GET" else getSpecificIP(given_ip) # Assumes POST based on checks.

    # If all assertion test is passed, create a blueprint (dictionary).
    ip_info = {}

    if req_ip_data: # Checks if has content.
        if list(req_ip_data.keys()) != errorFields and list(req_ip_data.keys()) != rateLimitedFields: # Ensure that the given response doesn't contain fields declared under `errorFields` and `rateLimitedFields`.
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
    return render_template('index.html', ip_context = ip_query(None, "GET"))


@app.route("/", methods=['POST'])
def searchIP():
    # For test purposes, use "request.json.get()" instead. Error is not handled here.
    ip_address = request.json.get("ip_address")
    # ip_address = request.form.get('ip_address') # Before

    return render_template('index.html', ip_context = ip_query(ip_address, "POST"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
