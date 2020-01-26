from post_elasticsearch import data_generation
from random import random
from datetime import datetime
import time

sentiments = {
    0: "anger",
    1: "contempt",
    2: "disgust",
    3: "fear",
    4: "happiness",
    5: "neutral",
    6: "sadness",
    7: "surprise"
}

generate = ""
j = 0
for i in range(2000):
    if i % 25 == 0:
        j = 0
    json_object = {
        "sentiment":    sentiments[int(generate[j])],
        "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2000 - i)).isoformat()
    }
    data_generation(json_object)
    j = j + 1
    # print(json_object)
    # print(datetime.fromtimestamp(datetime.now().timestamp() - 50000 * random()).isoformat())


