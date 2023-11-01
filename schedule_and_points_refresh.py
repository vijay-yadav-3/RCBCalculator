import http.client
import json
import sys

conn = http.client.HTTPSConnection("cricbuzz-cricket.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': sys.argv[1],
    'X-RapidAPI-Host': "cricbuzz-cricket.p.rapidapi.com"
}
conn.request("GET", "/series/v1/6732", headers=headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
f = open("schedule.json", "w")
f.write(data.decode("utf-8"))
f.close()

conn.request("GET", "/stats/v1/series/6732/points-table", headers=headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
f = open("points.json", "w")
f.write(data.decode("utf-8"))
f.close()
