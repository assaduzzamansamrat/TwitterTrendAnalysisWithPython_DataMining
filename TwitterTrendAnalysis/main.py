import json


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
tempworldtrends = []
worldtrends = []
finalworldtrends = []
tempusTrends = []
usTrends = []
finalusTrends = []
with open('20230512_twitter_world_trends.json', 'r') as json_File:
    worldTrends = json.load(json_File)

with open('20230512_twitter_us_trends.json', 'r') as json_File:
        usTrends = json.load(json_File)

for wtrends in worldTrends:
    tempworldtrends.append(wtrends['trends'])
    for i in range(len(tempworldtrends)):
        for j in range(len(tempworldtrends[i])):
                 finalworldtrends.append(tempworldtrends[i][j]['name'])

for utrends in usTrends:
    tempusTrends.append(utrends['trends'])
    for i in range(len(tempusTrends)):
        for j in range(len(tempusTrends[i])):
            finalusTrends.append(tempusTrends[i][j]['name'])
common_member(finalworldtrends,finalusTrends)
print(finalworldtrends)
print(finalusTrends)