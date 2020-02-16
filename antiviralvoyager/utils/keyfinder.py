import requests, os, json

# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
DIR = os.path.dirname(__file__) or '.'

def get_iam_token(apikey):

    # Get an IAM token from IBM Cloud
    url     = "https://iam.bluemix.net/oidc/token"
    headers = { "Content-Type" : "application/x-www-form-urlencoded" }
    data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    IBM_cloud_IAM_uid = "bx"
    IBM_cloud_IAM_pwd = "bx"
    response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
    iam_token = response.json()["access_token"]
    return iam_token

if __name__ == '__main__':
    #print(get_iam_token())
    pass
