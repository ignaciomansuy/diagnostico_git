from collections import defaultdict
from datetime import datetime

def top10_retweeted(jsons_list):
    print(sorted(jsons_list, key=lambda json_: json_["retweetCount"])[:10])

def top10_most_comments(jsons_list):
    dict_count = defaultdict(int)
    map(lambda json_: dict_count[json_["user"]["id"]] += 1, jsons_list)
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    print(top10)

def top10_days(jsons_list):
    dict_count = defaultdict(int)
    def get_date(string):
        #2021-03-30T03:33:46+00:00
        date_ = datetime.strptime("2021-03-30T03:33:46+00:00", "%Y-%m-%dT%H:%M:%S%z")
        return date_.strftime("%d-%b-%Y")

    map(lambda json_: dict_count[get_date(json_["date"])] += 1, jsons_list)
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    print(top10)

