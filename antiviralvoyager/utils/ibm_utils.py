import requests, json, os
from utils import keyfinder

DIR = os.path.dirname(__file__) or '.'
f = open(DIR + "/../secrets.json")
secrets = json.loads(f.read())
f.close()

iam_token = keyfinder.get_iam_token(secrets['ibm_key'])
ml_instance_id = secrets['ibm_mliid']

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}


def query_US(illness_year, illness_month, illness_state, illness_setting, disaster_state, disaster_year, disaster_type):
    vals = [int(illness_year), int(illness_month), illness_state.upper(), illness_setting.upper(), disaster_state.upper(), int(disaster_year), disaster_type.upper()]
    payload_scoring = {"input_data": [{"fields": ["Illness_ Year", "Illness_Month", "Illness_State", "Illness_Setting", "Disaster_state", "Disaster_Year", "Disaster"], "values": [vals]}]}

    return score_prediction('https://us-south.ml.cloud.ibm.com/v4/deployments/be2dd1a1-cdff-4db8-8f79-90fe9c390927/predictions', payload_scoring)


# def query_China(year, week, flood_count):
#     vals = [year, week, flood_count]
#     payload_scoring = {"input_data": [{"fields": ["year", " week", " flood count"], "values": [vals]}]}

#     return score_prediction('https://us-south.ml.cloud.ibm.com/v4/deployments/aa9d40e6-9fb8-4139-94fc-c23da0a5bf33/predictions', payload_scoring)

def query_VolcanicEarthquake(Latitude, Longitude, Elevation, VolType, VEI):
    vals = [float(Latitude), float(Longitude), float(Elevation), VolType, int(VEI)]

    payload_scoring = {"input_data": [
        {"fields": ["Latitude", "Longitude", "Elevation", "Type", "Volcano Explosivity Index (VEI)"],
         "values": [vals]}]}

    #return score_prediction("https://us-south.ml.cloud.ibm.com/v4/deployments/6651a51d-eb29-4d34-93b5-db50756fd24a/predictions", payload_scoring)
    response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/v4/deployments/1d169fa3-2512-4586-92e2-a5cbbe7e0115/predictions", json=payload_scoring, headers=header)
    return json.loads(response_scoring.text)


def query_VolcanicTsunami(Latitude, Longitude, Elevation, VolType, VEI):
    vals = [1, float(Latitude), float(Longitude), float(Elevation), VolType, int(VEI)]

    payload_scoring = {"input_data": [
        {"fields": ["Earthquake", "Latitude", "Longitude", "Elevation", "Type", "Volcano Explosivity Index (VEI)"],
         "values": [vals]}]}

    #return score_prediction("https://us-south.ml.cloud.ibm.com/v4/deployments/6651a51d-eb29-4d34-93b5-db50756fd24a/predictions", payload_scoring)
    response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/v4/deployments/6651a51d-eb29-4d34-93b5-db50756fd24a/predictions", json=payload_scoring, headers=header)
    return json.loads(response_scoring.text)


def score_prediction(url, payload_scoring):
    response_scoring = requests.post(url, json=payload_scoring, headers=header)
    return json.loads(response_scoring.text)['predictions'][0]['values'][0][0]

if __name__ == '__main__':
    print(query_US(1998, 8, "Nebraska", "City", "Nebraska", 1998, "Tornado"))
    print(query_US(1998, 8, "Nebraska", "City", "Nebraska", 1998, "Earthquake"))
    print(query_US(1998, 8, "Nebraska", "City", "Nebraska", 1998, "Hurricane"))
    print(query_US(1998, 8, "Nebraska", "City", "Nebraska", 1998, "Hurricane Sandy"))
    print(query_US(1998, 8, "Nebraska", "City", "Nebraska", 1998, "Hurricane Katrina"))

    print('========================================')

    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Tornado"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Volcano"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Potato"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "T"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Hurricane"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Hurricane Sandy"))
    print(query_US(2012, 8, "Nebraska", "City", "Nebraska", 2012, "Hurricane Katrina"))

    # for i in range(2010, 2030, 1):
    #     print(i, ": ", query_China(i, 3, 0))
    #print(query_China(2025, 3, 999999999))
