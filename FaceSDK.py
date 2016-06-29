########### Python 2.7 #############
import httplib, urllib, base64, binascii, json
from PIL import Image
import requests
from StringIO import StringIO

API_KEY = '38a7f2282ac346f794c346640c4fc42a'
BASE_URL = 'api.projectoxford.ai'


#
# GENERAL
#
def sendRequest(requestType, url, params=None, body=None, headers=None):
    if params == None:
        params = urllib.urlencode({})

    if body == None:
        body = ""

    if headers == None:
        headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': API_KEY,
        }

    try:
        conn = httplib.HTTPSConnection(BASE_URL)
        request_url = "{0}?".format(url)
        conn.request(requestType, request_url + "%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return None

def extractValueForKey(key, jsonDict):
    if key == None or jsonDict == None:
        return None
    try:
        dictionary = json.loads(jsonDict)
        value = dictionary[key]
        return value
    except:
        print "Error extracting value from key"
        return None

def jsonToDict(jsonDict):
    if jsonDict == None:
        return None

    try:
        dictionary = json.loads(jsonDict)
        return dictionary
    except:
        print "Error converting json to dict"
        return None

#
# PERSON GROUPS API
#

def createPersonGroup(groupId, userData = ""):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    headers = None
    params = None
    body = '''
    {{
    "name":"{0}",
    "userData":"{1}"
    }}
    '''.format(groupId,userData)

    return sendRequest("PUT", url, params, body, headers)

def deletePersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    
    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = None

    sendRequest("DELETE", url, params, body, headers)

def getPersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}".format(groupId)
    
    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = None

    sendRequest("GET", url, params, body, headers)

def getPersonGroupTrainingStatus(groupId):
    url = "/face/v1.0/persongroups/{}/training".format(groupId)
    
    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    print sendRequest("GET", url, params, body, headers)

def listPersonGroups():
    url = "/face/v1.0/persongroups"
    
    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = None

    return sendRequest("GET", url, params, body, headers)

def trainPersonGroup(groupId):
    url = "/face/v1.0/persongroups/{}/train".format(groupId)
    
    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = None

    print sendRequest("POST", url, params, body, headers)

#
# PERSON API
#

# Returns PersonID
def createPerson(groupId, name, imageUrl):
    url = "/face/v1.0/persongroups/{}/persons".format(groupId)
    
    headers = None
    params = None
    body = '''
    {{
        "name":"{0}",
        "userData":"{1}"
    }}
    '''.format(name, imageUrl)

    retval = sendRequest("POST", url, params, body, headers)

    return extractValueForKey("personId", retval)

# returns persistedFaceId
def addFaceToPerson(groupId, personId, imageUrl):
    url = "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces".format(groupId, personId)

    headers = None
    params = None
    body = '''
    {{
        "url":"{0}"
    }}
    '''.format(imageUrl)

    retval = sendRequest("POST", url, params, body, headers)

    return extractValueForKey("persistedFaceId", retval)

def deletePerson(groupId, personId):
    url = "/face/v1.0/persongroups/{0}/persons/{1}".format(groupId, personId)

    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    retval = sendRequest("DELETE", url, params, body, headers)

    return retval

def deletePersonFace(groupId, personId, persistedFaceId):
    url = "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces/{2}".format(groupId, personId, persistedFaceId)

    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    retval = sendRequest("DELETE", url, params, body, headers)

    return retval

# returns dictionary of information
def getPerson(groupId, personId):
    url = "/face/v1.0/persongroups/{}/persons/{}".format(groupId, personId)

    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    retval = sendRequest("GET", url, params, body, headers)

    return jsonToDict(retval)

def getPersonFace(groupId, personId, persistedFaceId):
    url = "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces/{2}".format(groupId, personId, persistedFaceId)

    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    retval = sendRequest("GET", url, params, body, headers)

    return jsonToDict(retval)

def listPersonGroupMembers(groupId):
    url = "/face/v1.0/persongroups/{0}/persons".format(groupId)

    headers = {
    'Ocp-Apim-Subscription-Key': API_KEY
    }
    params = None
    body = None

    retval = sendRequest("GET", url, params, body, headers)

    return jsonToDict(retval)

def updatePerson(groupId, personId, name, imageUrl):
    url = "/face/v1.0/persongroups/{0}/persons/{1}".format(groupId, personId)
    
    headers = None
    params = None
    body = '''
    {{
        "name":"{0}",
        "userData":"{1}"
    }}
    '''.format(name, imageUrl)

    retval = sendRequest("PATCH", url, params, body, headers)

    return retval

def updatePersonFace(groupId, personId, persistedFaceId, userData):
    url = "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces/{2}".format(groupId, personId, persistedFaceId)
    
    headers = None
    params = None
    body = '''
    {{
        "userData":"{0}"
    }}
    '''.format(userData)

    retval = sendRequest("PATCH", url, params, body, headers)

    return retval

#
# FACE
#

# returns dict
# -> isIdentical: String
# -> confidence: String
def verifyFace(firstFaceId, secondFaceId):
    url ="/face/v1.0/verify"
    headers = None
    params = None
    body = '''
    {{
        "faceId1":"{0}",
        "faceId2":"{1}"
    }}
    '''.format(firstFaceId, secondFaceId)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)

# returns dict
# -> faceId: String
# -> candidates: [String] (ranked by confidence)
# -> personId: String
# -> confidence: String
def identifyFace(groupId, faceId, maxNumOfCandidatesReturnedates):
    url ="/face/v1.0/identify"
    headers = None
    params = None
    body = '''
    {{
        "personGroupId":"{0}",
        "faceIds":[
            "{1}" 
        ],
        "maxNumOfCandidatesReturned":{2} 
    }}
    '''.format(groupId, faceId, maxNumOfCandidatesReturnedates)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)

# returns dict
# -> faceId: String
# -> faceRectange: Object
def detectFaceFromUrl(imageUrl):
    url ="/face/v1.0/detect"
    headers = None
    params = None
    body = '''
    {{
        "url":"{}" 
    }}
    '''.format(imageUrl)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)

# returns dict
# -> faceId: String
# -> faceRectange: Object
def detectFaceFromData(imageFile):
    if imageFile == None:
        return None

    try:
        f = open(imageFile, "rb")
        imgdata = f.read()
        print "%s" % (binascii.hexlify(ima))
        f.close()
    except:
        print "Error reading image file"
        return None

    url ="/face/v1.0/detect"
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = '''
    {{
        "url":"{}" 
    }}
    '''.format(imagedata)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)

#
# FACE LISTS
#

def createFaceList(faceListId, userData):
    url = "/face/v1.0/facelists/{}".format(faceListId)
    headers = None
    params = None
    body = '''
    {{
        "name":"{0}",
        "userData":"{1}" 
    }}
    '''.format(faceListId, userData)

    retval = sendRequest("PUT", url, params, body, headers)

    return retval

def deleteFaceList(faceListId):
    url = "/face/v1.0/facelists/{}".format(faceListId)
    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY,
    }
    params = None
    body = None

    retval = sendRequest("DELETE", url, params, body, headers)

    return retval

def addFaceToFaceList(faceListId, imageUrl, userData):
    url = "/face/v1.0/facelists/{}/persistedFaces".format(faceListId)
    headers = None
    params = urllib.urlencode({
    # Request parameters
    'userData': '{}'.format(userData),
    })
    body = '''
    {{
        "url":"{0}", 
    }}
    '''.format(imageUrl)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)

def findSimilarFaces(faceId, faceListId, maxNumOfCandidatesReturned):
    url = "/face/v1.0/findsimilars"
    headers = None
    params = None
    body = '''
    {{
        "faceId":"{0}", 
        "faceListId":"{1}",
        "maxNumOfCandidatesReturned":{2}
    }}
    '''.format(faceId, faceListId, maxNumOfCandidatesReturned)

    retval = sendRequest("POST", url, params, body, headers)

    return jsonToDict(retval)




#
#  TESTING
#

#trainPersonGroup('test-people-group')
#print listPersonGroups()
#getPersonGroupTrainingStatus('test-people-group')
#getPersonGroup('test-people-group')
#print createPersonGroup('male-celebrities')
#deletePersonGroup('test-people-group')
# peterUrl = "http://ia.media-imdb.com/images/M/MV5BMTM1MTI5Mzc0MF5BMl5BanBnXkFtZTYwNzgzOTQz._V1_UY317_CR20,0,214,317_AL_.jpg"
# peterUrl2 = "http://assets.rollingstone.com/assets/images/artists/ice-t.jpg"

#personId = createPerson("male-celebrities", "Peter Dinklage", "http://ia.media-imdb.com/images/M/MV5BMTM1MTI5Mzc0MF5BMl5BanBnXkFtZTYwNzgzOTQz._V1_UY317_CR20,0,214,317_AL_.jpg")
#persistedFaceId = addFaceToPerson("male-celebrities", personId, peterUrl)
#print deletePersonFace("male-celebrities", personId, persistedFaceId)
#print getPersonFace("male-celebrities", personId, persistedFaceId)
#print updatePerson("male-celebrities", personId, "Neal Van Ness", "IMAGE URL!")

#print getPersonGroupTrainingStatus("male-celebrities")
#exit()

# print createFaceList("male-celebs", "face list user data")
# print addFaceToFaceList("male-celebs", peterUrl, "test data")

# detectFaceResults = detectFaceFromUrl(peterUrl2)

# print findSimilarFaces(detectFaceResults[0]["faceId"], "male-celebs", 1)

# print deleteFaceList("male-celebs")

# exit()


# print trainPersonGroup("male-celebrities")


# detectFaceResults = detectFaceFromUrl(peterUrl2)
# identifyFaceResults = identifyFace("male-celebrities", detectFaceResults[0]["faceId"], 1)
# getPersonResults = getPerson("male-celebrities", identifyFaceResults[0]["candidates"][0]["personId"])
# url = getPersonResults["userData"]

# #Image that was sent
# response = requests.get(peterUrl2)
# sentImg = Image.open(StringIO(response.content))
# sentImg.show()

# # Image result
# response = requests.get(url)
# resultsImg = Image.open(StringIO(response.content))
# resultsImg.show()


# print "With confidence of: {}".format(identifyFaceResults[0]["candidates"][0]["confidence"])

#members = listPersonGroupMembers("male-celebrities")
#for member in members:
#    print "deleting: ", member["name"]
#    deletePerson("male-celebrities", member["personId"])
