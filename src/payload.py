import requests as rq
from dotenv import load_dotenv
import os
from datetime import date as _date

# LOGIN URL VARIABLE
LOGIN_URL = "https://software.kmutnb.ac.th/login/"
LOGGEDIN_URL = "https://software.kmutnb.ac.th/download/"
ADOBE_PROCESS_URL = "https://software.kmutnb.ac.th/adobe-reserve/processa.php"

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


# Helper to compute the first day of the next month (with year rollover)
def make_date_expire(dt: _date) -> str:
    """
    Return a string in YYYY-MM-01 format representing the first day of the month
    following the given date `dt`. If `dt` is in January, adjust the year
    accordingly (previous-year logic from original code preserved: decrease year
    by 1 when month == 1).
    """
    if dt.month == 1:
        year = dt.year - 1
        month = 12
    else:
        year = dt.year
        month = dt.month + 1
    return f"{year:04d}-{month:02d}-01"


# HEADER AND DATA (Adobe Process - final endpoint)
ADOBE_URL = "https://software.kmutnb.ac.th:443/adobe-reserve/add2.php"
adobe_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Origin": "https://software.kmutnb.ac.th",
    "Referer": "https://software.kmutnb.ac.th/adobe-reserve/processa.php",
}

adobe_data = {
    "userId": "",
    "date_expire": make_date_expire(_date.today()),
    "status_number": "0",
    "Submit_get": "",
}

# USING SESSION FOR HOLD SESSION FOR GRANT ADOBE ACCESS
with rq.session() as rqss:
    rqss.post(LOGIN_URL, headers=payload_headers, data=payload_data, verify=False)
    req3 = rqss.post(ADOBE_URL, headers=adobe_headers, data=adobe_data, verify=False)
    print(req3.text)
