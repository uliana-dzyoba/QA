import hashlib
import os
import shutil
import sys
import requests

server_ip = sys.argv[1]
server_port = sys.argv[2]

url = 'http://'+server_ip+':'+server_port+'/'

path = os.path.join(os.path.abspath(os.sep), '/clientdata')
# path = '/home/uliana/QA/lab1/client/clientdata' #for test

response = requests.get(url, stream=True)
original_md5 = response.headers['checksum']
with open(path+'/textfile', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

with open(path+'/textfile', 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()

# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print("MD5 verified.")
else:
    print("MD5 verification failed!.")
    raise ValueError('checksum is wrong')

while(True):
    pass