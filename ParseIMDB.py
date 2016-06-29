########### Python 2.7 #############
import httplib, urllib2, base64, binascii, re, urllib
from PIL import Image
import cStringIO as StringIO

BASE_URL = "www.imdb.com"

def getTopList(gender, startIdx):
    url = "http://imdb.com/search/name?gender={0}&start={1}".format(gender, startIdx)

    try:
        response = urllib2.urlopen(url)
	html = response.read()
	people = re.findall(r'<a href="\/name\/(\w*)\/" title="([^"]*)">', html)
	for person in people:
	    print person
    except Exception as e:
        print("[Errno {}]".format(e))
    return people

def getImagesForPeople(people):
    for person in people:
        url = "http://imdb.com/name/{}/".format(person[0])

        try:
            response = urllib2.urlopen(url)
            html = response.read()
            img = re.findall('"([^"]*317_AL_.jpg)"', html)
            print img
            try:
                response = urllib.urlretrieve(img[0],"{0}/{1}.jpg".format("img", person[1]))
            except Exception as e:
                print(e)

        except Exception as e:
            print("[Errno {}]".format(e))

people = []
for i in xrange(20):
    people.extend(getTopList("male", 1 + 50 * i))
getImagesForPeople(people)
