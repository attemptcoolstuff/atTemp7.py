#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Scripted by 4tte3p7 Indev
# Please Read the Instructions Before Attempting to Run This Script, Otherwise It WILL NOT Function

import requests
import urllib
import json
import re
import datetime
import sys

# Two Mandatary Inputed Variables, Once Again, Please Read the Instructions
yourUserName = "input_your_encoded_username_here"
yourPassword = "input_your_encoded_password_here"

# One Optional Inputed Variable, Only If It Is Needed for This Script to Run Properly
yourInternalStudentID = ""




#1, Requesting for Student Login Access
login_url = "https://auth.xiaoyuanjijiehao.com/oauth2/token"
login_headers = {
    "Authorization": "Basic NTgyYWFhZTU5N2Q1YjE2ZTU4NjhlZjVmOmRiMzU3YmRiNmYzYTBjNzJkYzJkOWM5MjkzMmFkMDYyZWRkZWE5ZjY=",
    "Content-Type": "application/x-www-form-urlencoded",
    "VERSION": "3.8.6",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 6P Build/OPM2.171019.029.A1",
    "Host": "auth.xiaoyuanjijiehao.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "61"
}
login_data = {
    "grant_type": "password",
    "username": yourUserName,
    "password": yourPassword
}
login_data = urllib.parse.urlencode(login_data)
login_response = requests.post(login_url, headers = login_headers, data = login_data, verify = False)
# Making Fake IDKEY and X-ANT-TOKEN :3
# step1, Arranging
login_array = json.loads(login_response.text)
ACCESS_TOKEN_RAW = login_array["access_token"]
USER_ID = login_array["user_id"]
# step2, Crafting
ACCESS_TOKEN = "ACKEY_" + ACCESS_TOKEN_RAW
IDKEY = USER_ID + "_ACKEY_" + ACCESS_TOKEN_RAW
X_ANT_TOKEN = ACCESS_TOKEN_RAW
print("----------Receiving Login Message----------")
print (login_response.text)

# 2, Receiving WebPage Content In a Row, Acquiring All Its Content
# Actually, All It Needs is the Cookie
# round1
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/index.html"
wContent_headers = {
   "Host": "h5api.xiaoyuanjijiehao.com",
   "Connection": "keep-alive",
   "Pragma": "no-cache",
   "Cache-Control": "no-cache",
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM2.171019.029.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045132 Mobile Safari/537.36Ant-Android-WebView",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/tpg,*/*;q=0.8",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "zh-CN,en-US;q=0.9"
}
wContent_data = {}
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round1 Message----------")
print (wContent_response.text)
# After round1, It Is Now Able to Dump the Cookie
wContent_array = json.loads(json.dumps(dict(wContent_response.headers)))
wContent_cookieDumpingRule = re.compile(r'(.*?);', re.S)
wContent_cookie = re.findall(wContent_cookieDumpingRule, wContent_array["Set-Cookie"])[0]
print("----------Dumping the Cookie----------")
print(wContent_cookie)

# round2
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/css/app.9aa269cc.css"
wContent_headers = {
   "Host": "h5api.xiaoyuanjijiehao.com",
   "Connection": "keep-alive",
   "Pragma": "no-cache",
   "Cache-Control": "no-cache",
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM2.171019.029.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045132 Mobile Safari/537.36Ant-Android-WebView",
   "Accept": "text/css,*/*;q=0.1",
   "Referer": "https://h5api.xiaoyuanjijiehao.com/classbodyreport/index.html",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "zh-CN,en-US;q=0.9",
   "Cookie": wContent_cookie
}
wContent_data = {}
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round2 Message----------")
print (wContent_response.text)

# round3
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/css/npm.element-ui.1d0938a9.css"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round3 Message----------")
print (wContent_response.text)

# round4
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/css/npm.vant.b319fad3.css"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round4 Message----------")
print (wContent_response.text)

# round5
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/js/npm.core-js.0aa87aea.js"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round5 Message----------")
print (wContent_response.text)

# round6
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/js/npm.vant.7e49e1e8.js"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round6 Message----------")
print (wContent_response.text)

# round7
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/js/npm.element-ui.550eea97.js"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round7 Message----------")
print (wContent_response.text)

# round8
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/js/app.a1eac9ec.js"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent round8 Message----------")
print (wContent_response.text)

# Now the Cookie has Changed, So Replace It with the New One
print("----------Old Cookie----------")
print(wContent_cookie)
wContent_array = json.loads(json.dumps(dict(wContent_response.headers)))
wContent_cookieDumpingRule = re.compile(r'(.*?);', re.S)
wContent_cookie_original = wContent_cookie
wContent_cookie = re.findall(wContent_cookieDumpingRule, wContent_array["Set-Cookie"])[0]
print("----------New Cookie 2nd----------")
print(wContent_cookie)

# Final Round
wContent_headers = {
   "Host": "h5api.xiaoyuanjijiehao.com",
   "Connection": "keep-alive",
   "Pragma": "no-cache",
   "Cache-Control": "no-cache",
   "Upgrade-Insecure-Requests": "1",
   "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM2.171019.029.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045132 Mobile Safari/537.36Ant-Android-WebView",
   "Accept": "text/css,*/*;q=0.1",
   "Referer": "https://h5api.xiaoyuanjijiehao.com/classbodyreport/index.html",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "zh-CN,en-US;q=0.9",
   "Cookie": wContent_cookie
}
wContent_url = "https://h5api.xiaoyuanjijiehao.com/classbodyreport/version.js?v=1597497959421"
wContent_response = requests.get(wContent_url, headers = wContent_headers, data = wContent_data, verify = False)
print("----------Receiving wContent Final Round Message----------")
print (wContent_response.text)

# Now the Cookie has Changed AGAIN, So Simply Step In <3
print("----------Old Cookie----------")
print(wContent_cookie_original)
print("----------New Cookie 2nd----------")
print(wContent_cookie)
wContent_array = json.loads(json.dumps(dict(wContent_response.headers)))
wContent_cookieDumpingRule = re.compile(r'(.*?);', re.S)
wContent_cookie = re.findall(wContent_cookieDumpingRule, wContent_array["Set-Cookie"])[0]
print("----------New Cookie 3rd----------")
print(wContent_cookie)

# 3, Receiving Info About Check-In Time
# step1, Morning
checkInTime_url = "https://h5api.xiaoyuanjijiehao.com/api/staff/interface"
checkInTime_headers = {
   "Host": "h5api.xiaoyuanjijiehao.com",
   "Connection": "keep-alive",
   "Content-Length": "151",
   "Pragma": "no-cache",
   "Cache-Control": "no-cache",
   "Accept": "application/x-www-form-urlencoded",
   "Origin": "https://h5api.xiaoyuanjijiehao.com",
   "AccessToken": ACCESS_TOKEN,
   "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM2.171019.029.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045132 Mobile Safari/537.36Ant-Android-WebView",
   "Content-Type": "application/x-www-form-urlencoded",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "zh-CN,en-US;q=0.9",
   "Referer": "https://h5api.xiaoyuanjijiehao.com/classbodyreport/index.html",
   "Cookie": wContent_cookie,
   "X-Requested-With": "com.zjelite.antlinkercampus"
}
checkInTime_data = {
    "Router": "/api/system/getsystemparams",
    "Method": "POST",
    "Body": str("{\"SGroup\":\"function\",\"SType\":\"TemperatureUp\",\"vName\":\"TemperatureUpMorn\"}")
}
checkInTime_response = requests.post(checkInTime_url, headers = checkInTime_headers, json = checkInTime_data, verify = False)
print("----------Receiving Morning Check-In Time----------")
print (checkInTime_response.text)
# step2, Noon
checkInTime_data = {
    "Router": "/api/system/getsystemparams",
    "Method": "POST",
    "Body": str("{\"SGroup\":\"function\",\"SType\":\"TemperatureUp\",\"vName\":\"TemperatureUpNoon\"}")
}
checkInTime_response = requests.post(checkInTime_url, headers = checkInTime_headers, json = checkInTime_data, verify = False)
print("----------Recieving Noon Check-In Time----------")
print (checkInTime_response.text)
# step3, Night
checkInTime_data = {
    "Router": "/api/system/getsystemparams",
    "Method": "POST",
    "Body": str("{\"SGroup\":\"function\",\"SType\":\"TemperatureUp\",\"vName\":\"TemperatureUpNight\"}")
}
checkInTime_response = requests.post(checkInTime_url, headers = checkInTime_headers, json = checkInTime_data, verify = False)
print("----------Receiving Night Check-In Time----------")
print (checkInTime_response.text)
# step4, Outside the Campus
checkInTime_data = {
    "Router": "/api/system/getsystemparams",
    "Method": "POST",
    "Body": str("{\"SGroup\":\"function\",\"SType\":\"TemperatureUp\",\"vName\":\"TemperatureUpOutSchool\"}")
}
checkInTime_response = requests.post(checkInTime_url, headers = checkInTime_headers, json = checkInTime_data, verify = False)
print("----------Receiving OutSchool Check-In Time----------")
print (checkInTime_response.text)

# 4, Time Configuration, Student Info Receiving
# Setting the Interval All Day Long, Why Not xD
time_real = datetime.datetime.now()
time_output = ""

if datetime.datetime.strptime(str(datetime.datetime.now().date()) + '0:00', '%Y-%m-%d%H:%M') <= time_real and time_real <= datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M'):
    time_output = "07:00-09:00"

elif datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:01', '%Y-%m-%d%H:%M') <= time_real and time_real <= datetime.datetime.strptime(str(datetime.datetime.now().date()) + '17:00', '%Y-%m-%d%H:%M'):
    time_output = "11:00-13:00"
    
else:
    time_output = "21:00-23:00"
    
print("----------Time Configuration----------")
print(time_output)
stdInfo_body = str("{\"ClassCode\":\"\",\"Times\":\"" + time_output + "\"}""")
stdInfo_url = checkInTime_url
stdInfo_headers = checkInTime_headers
# There Are Two APIs, So It Is More Complicated Than It Should Be
# The IntelUserCode Is Actually FIXED, So It Is Pretty Easy to Bypass Theses Codelines

# API: /api/temperatureup/querynoup, Becomes Null When Check-In Is Completed

intelUserCode = yourInternalStudentID
try:
    stdInfo_data = {
        "Router": "/api/temperatureup/querynoup",
        "Method": "POST",
        "Body": stdInfo_body
    }
    stdInfo_response = requests.post(stdInfo_url, headers = stdInfo_headers, json = stdInfo_data, verify = False)
    print("----------Receiving Student Info----------")
    print (stdInfo_response.text)
    # Dumping the Interval StudentID
    stdInfo_array = json.loads(stdInfo_response.text)
    intelUserCode = stdInfo_array["Data"]["dataOut"][0]['IntelUserCode']
    print("----------Dumping Student ID----------")
    print (intelUserCode)
except TypeError:
    # API: /api/temperatureup/querynoup dataIn
    try:
        stdInfo_data = {
            "Router": "/api/temperatureup/querynoup",
            "Method": "POST",
            "Body": stdInfo_body
        }
        stdInfo_response = requests.post(stdInfo_url, headers = stdInfo_headers, json = stdInfo_data, verify = False)
        print("----------Receiving Student Info----------")
        print (stdInfo_response.text)
        # Dumping the Interval StudentID
        stdInfo_array = json.loads(stdInfo_response.text)
        intelUserCode = stdInfo_array["Data"]["dataIn"][0]['IntelUserCode']
        print("----------Dumping Student ID----------")
        print (intelUserCode)

    except TypeError:
    # API: /api/temperatureup/queryuped
        try:
            stdInfo_data = {
                "Router": "/api/temperatureup/queryuped",
                "Method": "POST",
                "Body": stdInfo_body
            }
            stdInfo_response = requests.post(stdInfo_url, headers = stdInfo_headers, json = stdInfo_data, verify = False)
            print("----------Receiving Student Info----------")
            print (stdInfo_response.text)
            # Dumping the Interval StudentID
            stdInfo_array = json.loads(stdInfo_response.text)
            intelUserCode = stdInfo_array["Data"][0]['IntelUserCode']
            print("----------Dumping Student ID----------")
            print (intelUserCode)
        
        except TypeError:
            if intelUserCode == "":
                print("Failed to Receive IntelUserCode, Please Enter IntelUserCode Manually")
                sys.exit(0)
# 5, Finally, Submit As If This is Done All on a Phone
stdInfo_body = str("{\"user\":\"" + intelUserCode + "\",\"temperature\":\"1\",\"reportArea\":\"山东省青岛市市南区\",\"memo\":\"\"}""")
stdInfo_url = checkInTime_url
stdInfo_headers = checkInTime_headers
stdInfo_data = {
    "Router": "/api/studentncpback/puttemperature",
    "Method": "POST",
    "Body": stdInfo_body
}
stdInfo_response = requests.post(stdInfo_url, headers = stdInfo_headers, json = stdInfo_data, verify = False)
print("----------Receiving Submitting Result----------")
print (stdInfo_response.text)
