from flask import Flask, redirect, url_for, render_template, request
from api import getSpecificIP, getIP
import os

app = Flask(__name__, template_folder='.')


@app.route("/", methods=['GET'])
def home():
    ip_address = "192.168.254.1"
    ip_version = "ipv4"
    ip_region = "Manila"
    ip_postal_code = "1800"
    ip_country = "Philippines"
    ip_timezone = "Asia/Manila"
    ip_calling_code = "+63"
    ip_asn = "AS132199"
    ip_isp = "PLDT Inc."
    ip_lat = 14.674
    ip_lng = 121.014
    return render_template('index.html',
                           ip_address=ip_address,
                           ip_version=ip_version,
                           ip_region=ip_region,
                           ip_postal_code=ip_postal_code,
                           ip_country=ip_country,
                           ip_timezone=ip_timezone,
                           ip_calling_code=ip_calling_code,
                           ip_asn=ip_asn,
                           ip_isp=ip_isp,
                           ip_lat=ip_lat,
                           ip_lng=ip_lng)


@app.route("/", methods=['POST'])
def searchIP():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
