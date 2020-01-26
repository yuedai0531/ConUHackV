import requests
from requests.auth import HTTPBasicAuth


def data_generation(json_object):
    es_url = "https://e54e0b68099e4fb7b4af7f6ab3ea778e.us-east-1.aws.found.io:9243"
    doc_index = "sentiment_flow_demo"
    doc_type = "data"

    headers = {
        "Content-Type": "application/json"
    }

    request_url = es_url + "/" + doc_index + "/" + doc_type

    r = requests.post(
        url=request_url,
        auth=HTTPBasicAuth("elastic", "ieQEE5Q4UHVRDOwICsizTDSX"),
        json=json_object,
        headers=headers)
    # print(r.text)
