from flask import Flask, send_from_directory, abort
import os
import random
import string
import hashlib

n = 1024 # 1 Kb of text
chars = ''.join([random.choice(string.ascii_letters) for i in range(n)])

path = os.path.join(os.path.abspath(os.sep), '/serverdata')
# path = '/home/uliana/QA/lab1/server/serverdata' #for test
if not os.path.exists(path):
    print('doesnt exist')

with open(path+'/textfile.txt', 'w+') as f:
    f.write(chars)

app = Flask(__name__)

@app.route('/')
def index():
    with open(path+'/textfile.txt', 'rb') as file_to_proccess:
        # read contents of the file
        data = file_to_proccess.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()
    try:
        response = send_from_directory(directory=path, path='textfile.txt')
        response.headers['checksum'] = md5_returned
        return response
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))