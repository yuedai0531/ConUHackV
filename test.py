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
#
# generate = ""
# j = 0
# for i in range(2000):
#     if i % 25 == 0:
#         j = 0
#     json_object = {
#         "sentiment":    sentiments[int(generate[j])],
#         "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2000 - i)).isoformat()
#     }
#     data_generation(json_object)
#     j = j + 1
#     # print(json_object)
#     # print(datetime.fromtimestamp(datetime.now().timestamp() - 50000 * random()).isoformat())


for i in range(0, 2100):
    if 0<=i<300: #day1
        if 0<=i<150: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
            print(i)
        elif 150<=i<200: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 200<=i<240: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 240<=i<300: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)

    print(i)

    if 300<=i<600: #day2
        if 300<=i<400: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 400<=i<480: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 480<=i<540: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 540<=i<600: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
    print(i)

    if 600<=i<900: #day3
        if 600<=i<710: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 710<=i<800: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 800<=i<850: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 850<=i<900: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)

    print(i)

    if 900<=i<1200: #day4
        if 900<=i<1010: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1010<=i<1090: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1090<=i<1120: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1120<=i<1200: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)

    print(i)
    if 1200<=i<1500: #day5
        if 1200<=i<1320: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1320<=i<1390: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1390<=i<1460: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1460<=i<1500: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)

    print(i)
    if 1500<=i<1800: #day6
        if 1500<=i<1650: #100 happies
            json_object = {
                "sentiment":    "happiness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1650<=i<1725: #50 sads
            json_object = {
                "sentiment":    "sadness",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1725<=i<1750: #20 angry
            json_object = {
                "sentiment":    "anger",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        elif 1750<=i<1800: #30 fear
            json_object = {
                "sentiment":    "fear",
                "timestamp":    datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
            }
            data_generation(json_object)
        print(i)
        if 1800 <= i < 2100:  # day7
            if 1800 <= i < 2000:  # 100 happies
                json_object = {
                    "sentiment": "happiness",
                    "timestamp": datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
                }
                data_generation(json_object)
            elif 2000 <= i < 2040:  # 50 sads
                json_object = {
                    "sentiment": "sadness",
                    "timestamp": datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
                }
                data_generation(json_object)
            elif 2040 <= i < 2070:  # 20 angry
                json_object = {
                    "sentiment": "anger",
                    "timestamp": datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
                }
                data_generation(json_object)
            elif 2070 <= i < 2100:  # 30 fear
                json_object = {
                    "sentiment": "fear",
                    "timestamp": datetime.fromtimestamp(datetime.now().timestamp() - 250 * (2100 - i)).isoformat()
                }
                data_generation(json_object)
