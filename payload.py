import requests as rq
from dotenv import load_dotenv
import os

# LOGIN URL VARIABLE
login_url = "https://software.kmutnb.ac.th/login/"
loggedin_url = "https://software.kmutnb.ac.th/download/"
adobe_url = "https://software.kmutnb.ac.th/adobe-reserve/processa.php"

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

# GET USERNAME AND PASSWORD FROM ENVIRONMENT VARIABLES
username = os.getenv("KMUTNB_USERNAME")
password = os.getenv("KMUTNB_PASSWORD")

# HEADERS PAYLOAD
payload_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Origin": "https://software.kmutnb.ac.th",
    "Referer": "https://software.kmutnb.ac.th/login/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# DATA PAYLOAD
payload_data = {"myusername": username, "mypassword": password, "Submit": ""}

# HEADER AND DATA (Adobe Process)
adobe_url = "https://software.kmutnb.ac.th:443/adobe-reserve/add2.php"
adobe_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Origin": "https://software.kmutnb.ac.th",
    "Referer": "https://software.kmutnb.ac.th/adobe-reserve/processa.php",
}

adobe_data = {
    "userId": "",
    "date_expire": "2025-10-01",
    "status_number": "0",
    "Submit_get": "",
}

# USING SESSION FOR HOLD SESSION FOR GRANT ADOBE ACCESS
with rq.session() as rqss:
    rqss.post(login_url, headers=payload_headers, data=payload_data, verify=False)
    req3 = rqss.post(adobe_url, headers=adobe_headers, data=adobe_data, verify=False)
    print(req3.text)
