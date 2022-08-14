from collections import defaultdict

def top10_retweeted(jsons_list):
    print(sorted(jsons_list, key=lambda json_: json_["retweetCount"])[:10])

def top10_most_comments(jsons_list):
    dict_count = defaultdict(int)
    map(lambda json_: dict_count["user"]["id"] += 1, jsons_list)
    top10 = list(dict_count.items()).sort(key=lambda item: item[1])[:10]
    top10_ids = [item[0] for item in top10]
    print(top10_ids)


