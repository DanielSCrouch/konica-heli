
import requests
import random
from optparse import OptionParser

from err import RegisterError, AuthError


class Helicopter(object):
    """HTTP RestAPI Client for querying Konica RestAPI"""

    def __init__(self, **kwargs):
        """Initialise client with destination server address and port"""
        self.addr = kwargs.get('addr')
        self.port = kwargs.get('port')
        self.headers = {"Content-Type": "application/json",
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive"}
        self.token = None
        self.pad_id = None
        self.heli_name = random.randint(1, 10) # replace with UUID 

    def register(self, username='heli1', password='qwerty'):
        """Register username and password with API server"""
        url = "http://%s:%s%s" % (self.addr, self.port, '/register')
        payload = {"username": "user1", "password": "qwerty"}
        print("POST:", url)

        r = requests.post(url,
                          json=payload,
                          headers=self.headers)
        print('register response:', r.json())
        if r.status_code == 409:
            print("User already exists.")
        elif r.status_code != 201:
            raise RegisterError("User registration failed.")

    def authenticate(self):
        """Authenticate user with server, store access"""
        url = "http://%s:%s%s" % (self.addr, self.port, '/auth')
        payload = {"username": "user1", "password": "qwerty"}
        print("POST:", url)

        r = requests.post(url,
                          json=payload,
                          headers=self.headers)
        data = r.json()
        print(data)
        # fdata = {k.decode("utf-8"): data[k].decode("utf-8")
        #          for k in data.keys()}
        # print(fdata)
        if 'access_token' in data.keys():
            self.token = "JWT " + data['access_token']
            self.headers['Authorization'] = self.token
        else:
            raise AuthError("Unable to authenticate heli.")

    def request_land(self):
        """Request to land"""
        url = "http://%s:%s%s" % (self.addr, self.port, '/heli')
        print("GET:", url)
        r = requests.get(url, headers=self.headers)
        data = r.json() 
        if r.status_code == 200:
            self.pad_id = data['pad_id']
            print('cleared to land.')
        else:
            print('landing request refused') 
    
    def land(self): 
        """Land on helipad"""
        url = "http://%s:%s%s" % (self.addr, self.port, '/heli/' + str(self.pad_id))
        payload = {"heli_name": self.heli_name}
        print("POST:", url)

        r = requests.post(url, json=payload, headers=self.headers)

        data = r.json()
        print(data)

    def leave(self):
        """Send deploy request to API Gateway"""
        url = "http://%s:%s%s" % (self.addr, self.port, '/heli' + str(self.pad_id))
        payload = {"heli_name": self.heli_name}
        print("POST:", url)

        r = requests.delete(url, json=payload, headers=self.headers)

        data = r.json()
        print(data)


###############################################################################
# Main call option parsing
###############################################################################


def parseargs():
    p = OptionParser()
    p.add_option("-a",
                 dest="addr",
                 help="Specify the host server address",
                 metavar="opt",
                 default="127.0.0.1")
    p.add_option("-p",
                 dest="port",
                 help="Specify the server port",
                 metavar="opt",
                 default="5000")
    o, a = p.parse_args()
    return o

###############################################################################
# Main
###############################################################################


if __name__ == '__main__':
    o = parseargs()
    try:
        client = Helicopter(**o.__dict__)
        client.register()
        client.authenticate()
        client.request_land()
        client.land() 
        client.leave() 
        # client.close()
    except Exception as e:
        print("Exception:", e)
        exit(-1)
    exit(0)
