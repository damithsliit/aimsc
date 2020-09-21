from flask import Flask,request
from urllib.request import urlopen


app = Flask(__name__)

@app.route("/pref", methods=['GET'])
def query_strings():

    qq = request.args['search']
    print(qq)
    with urlopen('https://www.googleapis.com/youtube/v3/search?q='+qq+'&safeSearch=strict&alt=json&key=AIzaSyDAK5MbpcuM-GbmmSA9ySjg6UU3cvUhe_s') as r:
        text = r.read()
    return text
  

# def searchq(qq):
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

#     # Get credentials and create an API client
#     flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#         client_secrets_file, scopes)
#     credentials = flow.run_console()
#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, credentials=credentials)

#     request = youtube.search().list(
#         q=qq,
#         safeSearch="strict",
#         alt="json"
#     )
#     response = request.execute()

#     print(response)

# searchq("hello")

if __name__ == "__main__":
  app.run()

