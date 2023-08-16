"""
划分云南乡镇街道
"""
import pprint
# from collections import defaultdict

mapping = {}
with open("yunnan.txt", encoding='UTF-8') as f:
    for line in f:
        country, province, prefecture, county, *township = line.strip().split()
        mapping.setdefault(province, [])
        mapping[province].extend(township)
        mapping[province].append(county)
        mapping.setdefault(prefecture, [])
        mapping[prefecture].extend(township)
        mapping[province].append(county)
        mapping.setdefault(county, [])
        mapping[county].extend(township)
pprint.pprint(mapping)
