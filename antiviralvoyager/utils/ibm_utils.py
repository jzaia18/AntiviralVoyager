import urllib3, requests, json, os
import keyfinder

DIR = os.path.dirname(__file__) or '.'
f = open(DIR + "/../secrets.json")
secrets = json.loads(f.read())
f.close()

iam_token = keyfinder.get_iam_token(secrets['ibm_key'])
ml_instance_id = secrets['ibm_mliid']

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}


def query_US(illness_year, illness_month, illness_state, illness_setting, disaster_state, disaster_year, disaster_type):
    vals = [illness_year, illness_month, illness_state, illness_setting, disaster_state, disaster_year, disaster_type]
    payload_scoring = {"input_data": [{"fields": ["Illness_ Year", "Illness_Month", "Illness_State", "Illness_Setting", "Disaster_state", "Disaster_Year", "Disaster"], "values": [vals]}]}

    return score_prediction('https://us-south.ml.cloud.ibm.com/v4/deployments/ab69f45e-1ba7-43b8-907c-ed969c5eaaf5/predictions', payload_scoring)


def query_China(year, week, flood_count):
    vals = [year, week, flood_count]
    payload_scoring = {"input_data": [{"fields": ["year", " week", " flood count"], "values": [vals]}]}

    return score_prediction('https://us-south.ml.cloud.ibm.com/v4/deployments/aa9d40e6-9fb8-4139-94fc-c23da0a5bf33/predictions', payload_scoring)

def query_VolcanicTsunami(Latitude, Longitude, Elevation, VEI):
    vals = [1, Latitude, Longitude, Elevation, "Caldera", VEI]

    payload_scoring = {"input_data": [
        {"fields": ["Earthquake", "Latitude", "Longitude", "Elevation", "Type", "Volcano Explosivity Index (VEI)"],
         "values": [vals]}]}

    return score_prediction("https://us-south.ml.cloud.ibm.com/v4/deployments/6651a51d-eb29-4d34-93b5-db50756fd24a/predictions", payload_scoring)


def score_prediction(url, payload_scoring):
    response_scoring = requests.post(url, json=payload_scoring, headers=header)
    return json.loads(response_scoring.text)['predictions'][0]['values'][0][0]

if __name__ == '__main__':
    print(query_US(1989, 8, "Nebraska", "Hotel", "Nebraska", 1989, "Tornado"))
    for i in range(2010, 2030, 1):
        print(i, ": ", query_China(i, 3, 0))
    #print(query_China(2025, 3, 999999999))
