import requests as rq
from dotenv import load_dotenv, dotenv_values
import os

# LOGIN URL VARIABLE
login_url = "https://software.kmutnb.ac.th/login/"
loggedin_url = "https://software.kmutnb.ac.th/download/"
adobe_url = "https://software.kmutnb.ac.th/adobe-reserve/processa.php"

# EXAMPLE .ENV FILE

# .env
# KMUTNB_USERNAME=s66xxxxxxxxxxx
# KMUTNB_PASSWORD=wtfisthisuniversity

# DIRECTORY OF FILE
# -- adobe-kmutnb
# |
# - > .env
# - > payload.py

# ENV FILE STUFF

load_dotenv()

username = os.getenv("KMUTNB_USERNAME")
password = os.getenv("KMUTNB_PASSWORD")

# HEADERS PAYLOAD // IDK WHY ITS WORKING =_=
payload_headers = {
        "Cache-Control": "max-age=0", 
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"", 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"", 
        "Upgrade-Insecure-Requests": "1", 
        "Origin": "https://software.kmutnb.ac.th", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://software.kmutnb.ac.th/login/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "th-TH,th;q=0.9", "Connection": "close"}

# DATA PAYLOAD // GRAB FROM .ENV FILE
payload_data = { "myusername": username, "mypassword": password, "Submit": ''} 


# HEADER AND DATA (Adobe Process)
adobe_url = "https://software.kmutnb.ac.th:443/adobe-reserve/add2.php"
adobe_headers = {
                 "Cache-Control": "max-age=0",
                 "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
                 "Sec-Ch-Ua-Mobile": "?0", 
                 "Sec-Ch-Ua-Platform": "\"Windows\"", 
                 "Upgrade-Insecure-Requests": "1", 
                 "Origin": "https://software.kmutnb.ac.th", 
                 "Content-Type": "application/x-www-form-urlencoded", 
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", 
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                 "Sec-Fetch-Site": "same-origin", 
                 "Sec-Fetch-Mode": "navigate", 
                 "Sec-Fetch-User": "?1", 
                 "Sec-Fetch-Dest": "document", 
                 "Referer": "https://software.kmutnb.ac.th/adobe-reserve/processa.php", 
                 "Accept-Encoding": "gzip, deflate, br", 
                 "Accept-Language": "th-TH,th;q=0.9", 
                 "Connection": "close"}

adobe_data = {"userId": '', "date_expire": "2024-02-19", "status_number": "0", "Submit_get": ''}

# USING SESSION FOR HOLD SESSION FOR GRANT ADOBE ACCESS
with rq.session() as rqss:
    rqss.post(login_url, headers=payload_headers, data=payload_data, verify=False)
    req3 = qss.post(adobe_url, headers=adobe_headers, data=adobe_data,verify=False)
    print(req3.text)
