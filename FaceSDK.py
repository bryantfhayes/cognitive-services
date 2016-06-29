########### Python 2.7 #############
import httplib, urllib, base64, binascii
from PIL import Image
import cStringIO as StringIO

API_KEY = '38a7f2282ac346f794c346640c4fc42a'
BASE_URL = 'api.projectoxford.ai'

def createPersonGroup(groupId, userData = ""):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = '''
    {{
    "name":"{0}",
    "userData":"{1}"
    }}
    '''.format(groupId,userData)

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("PUT", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def deletePersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    headers = {
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = ""

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("DELETE", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getPersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    headers = {
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = ""

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("GET", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getPersonGroupTrainingStatus(groupId):
    url = "/face/v1.0/persongroups/{}/training".format(groupId)
    headers = {
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = ""

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("GET", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def listPersonGroups():
    url = "/face/v1.0/persongroups"
    headers = {
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = ""

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("GET", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def trainPersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}/train".format(groupId)
    headers = {
    #'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '38a7f2282ac346f794c346640c4fc42a',
    }
    params = urllib.urlencode({
    })
    body = ""

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request("POST", request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

#trainPersonGroup('test-people-group')
#listPersonGroups()
#getPersonGroupTrainingStatus('test-people-group')
#getPersonGroup('test-people-group')
#createPersonGroup('test-people-group')
#deletePersonGroup('test-people-group')


