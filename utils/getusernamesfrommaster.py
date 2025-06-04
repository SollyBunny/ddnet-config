#!/bin/env python3

import requests

url = "https://master4.ddnet.org/ddnet/15/servers.json"
response = requests.get(url)
data = response.json()

names = set()

for server in data.get("servers", []):
	for client in server.get("info", {}).get("clients"):
		name = client.get("name")
		if name:
			names.add(name)

with open("usernames.txt", "r") as file:
	for line in file.readlines():
		if line:
			names.add(line.strip())

with open("usernames.txt", "w") as file:
	for name in names:
		file.write(name)
		file.write("\n")
