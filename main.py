from flask import Flask,request
from urllib.request import urlopen
from waitress import serve


app = Flask(__name__)

@app.route("/pref", methods=['GET'])
def query_strings():

    qq = request.args['search']
    
    # calling the youtube API
    # API Key - AIzaSyDAK5MbpcuM-GbmmSA9ySjg6UU3cvUhe_s
    
    with urlopen('https://www.googleapis.com/youtube/v3/search?q='+qq+'&safeSearch=strict&alt=json&key=AIzaSyDAK5MbpcuM-GbmmSA9ySjg6UU3cvUhe_s') as r:
        text = r.read()
    return text

if __name__ == "__main__": 
    # aimsc API is running on localhost 5000 port
    app.run(host='127.0.0.1', port=5000)

