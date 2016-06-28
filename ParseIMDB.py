########### Python 2.7 #############
import httplib, urllib2, base64, binascii, re
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

getTopList("male", 51)
