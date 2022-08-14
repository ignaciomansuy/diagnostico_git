from collections import defaultdict

def top10_retweeted(jsons_list):
    print(sorted(jsons_list, key=lambda json_: json_["retweetCount"])[:10])





