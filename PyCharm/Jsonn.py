import json

data = '{"var1": "harry", "var2": 56}'  # he apan json madhe lihila ahe, this is json text
# print(data)
# # print(data["var1"]) #this is invalid, throws error
#
# parsed = json.loads(data)
# print(parsed , type(parsed))
# print(parsed['var1'])

data2 = {
    "channel_name": "CodeWith Harry",
    "cars": ['bmw', "monster", "audi A8"],
    "fridge": ("roti", "custard", 540),
    "isbad": False
}

jscomp = json.dumps(data2, sort_keys=True)  # json formatting pan hota for eg False is corrected to false (small f) json compatible
print(jscomp)
