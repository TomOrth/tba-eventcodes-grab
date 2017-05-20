import argparse
import requests
import json
import datetime

appId = "eventcodesgrab:grabbing event codes:0.1"
content = ""
year = datetime.datetime.now().year
 
parser = argparse.ArgumentParser(description='Get event codes from tba api')

parser.add_argument('--year', help='year to get event codes')

args = parser.parse_args()

if args.year:
    year = args.year

r = requests.get('https://www.thebluealliance.com/api/v2/events/' + year + "?X-TBA-App-Id=" + appId)

for data in r.json():
    content += data['name'] + ", " + data['key'] + '\n'
f = open('data.txt', 'w')
f.write(content)
f.close()
print(r.json())
