# import wikipedia


# #print(wikipedia.search("programming"))

# print(wikipedia.summary("Android"))
# #'features="html.parser"'

import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andhra Pradesh']['districtData']['Foreign Evacuees']['confirmed']
print("Active cases in South Andaman:", active_case);


# import requests
# import json
# response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
# #print(response_API.status_code)
# #data = response_API.text
# # parse_json = json.loads(data)
# # info = parse_json['description']
# # print("Info about API:\n", info)
# # key = parse_json['parameters']['key']['description']
# # print("\nDescription about the key:\n",key)