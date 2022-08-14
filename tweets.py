from collections import defaultdict
from datetime import datetime
import json


def top10_retweeted(jsons_list):
    print(sorted(jsons_list, key=lambda json_: json_["retweetCount"])[:10])

def top10_most_comments(jsons_list):
    dict_count = defaultdict(int)
    for json_ in jsons_list:
        dict_count[json_["user"]["id"]] += 1
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    print(top10)

def top10_days(jsons_list):
    dict_count = defaultdict(int)
    def get_date(string):
        #2021-03-30T03:33:46+00:00
        date_ = datetime.strptime("2021-03-30T03:33:46+00:00", "%Y-%m-%dT%H:%M:%S%z")
        return date_.strftime("%d-%b-%Y")

    for json_ in jsons_list:
        dict_count[get_date(json_["date"])] += 1
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    print(top10)

def top10_hastags(jsons_list):
    def get_hastags(tweet):
        return [string.strip() for string in tweet["content"].split('#')[1:]]
    dict_count = defaultdict(int)
    for tweet in jsons_list:
        for hash_ in get_hastags(tweet):
            dict_count[hash_] +=1
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    print(top10)


def main(json_file_name):
    with open(json_file_name) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    # the json file provided in https://www.kaggle.com/datasets/prathamsharma123/farmers-protest-tweets-dataset-raw-json
    # isn't a proper json, due to time I'm not implementing the conversion of that file to a easy to read json file
    # Here I asume that jsonObject is a list with all the jsons.
    top10_retweeted(jsonObject)
    top10_most_comments(jsonObject)
    top10_days(jsonObject)
    top10_hastags(jsonObject)